from flask import Flask,render_template,request,session
from hydra_redis import querying_mechanism
from hydrus.hydraspec import doc_maker

app = Flask(__name__)
app.secret_key = "any random string"

# @app.route('/')
# def index():
#     return render_template("index.html")
    
@app.route('/', methods= ['GET','POST'])
def enter_url():
    if request.method == 'GET':
        # print(render_template("index.html"))
        return render_template("index.html")
        # return '<html><h1>hello</h1></html>'
    if request.method == 'POST':
        if 'url' in request.form:
            url= request.form['url']
            session['url'] = url
            handle_data = querying_mechanism.HandleData()
            global api_doc
            endpoints = handle_data.load_data(url)
            session['entrypoint'] = endpoints
            apidoc1 = handle_data.load_data(url + "/vocab")
            api_doc = doc_maker.create_doc(apidoc1)
            global facades
            facades = querying_mechanism.QueryFacades(api_doc, session['url'],False)
            facades.initialize(True)
            print(url,endpoints)
            return render_template("index.html", apidoc = endpoints)
#        elif 'query' in request.form:
#            query = request.form['query']
#            print(query)
#            print(session['url'])
#            return render_template("index.html",apidoc)


@app.route('/query',methods=['GET','POST'])
def enter_query():
    if request.method == 'GET':
        return render_template("index.html")
    if request.method == 'POST':
        if 'query' in request.form:
            print("here")
            print(session['url'])
            query = request.form['query']
            print(query)
            output = facades.user_query(query)
            return render_template("index.html", query_output = output)
        return "NOT FOUND QUERY"

if __name__ == "__main__":
    app.run(debug=True)
    

