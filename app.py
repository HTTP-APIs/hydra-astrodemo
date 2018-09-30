from flask import Flask,render_template,request,session
from hydra_redis import querying_mechanism
from hydrus.hydraspec import doc_maker

app = Flask(__name__)
app.secret_key = "any random string"

history =[]

# @app.route('/')
# def index():
#     return render_template("index.html")
    
@app.route('/', methods= ['GET','POST'])
def enter_url():
    global history
    history = []
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
            global endpoints
            history.append(url)
            endpoints = handle_data.load_data(url)
            session['entrypoint'] = endpoints
            apidoc1 = handle_data.load_data(url + "/vocab")
            api_doc = doc_maker.create_doc(apidoc1)
            global facades
            facades = querying_mechanism.QueryFacades(api_doc, session['url'],False)
            check_url = str.encode(url)
            querying_mechanism.check_url_exist(check_url,facades)
            print(url,endpoints)
            return render_template("query.html", apidoc = endpoints, history=history)
#        elif 'query' in request.form:
#            query = request.form['query']
#            print(query)
#            print(session['url'])
#            return render_template("index.html",apidoc)


@app.route('/query',methods=['GET','POST'])
def enter_query():
    global history
    if request.method == 'GET':
        return render_template("query.html")
    if request.method == 'POST':
        if 'query' in request.form:
            print("here")
            query = request.form['query']
            print(query)
            history.append(query)
            history_rev = history[::-1]
            if len(history_rev)>5:
                history_rev.pop()
                history = history_rev[::-1]
            output = facades.user_query(query)
            return render_template("query.html", apidoc = endpoints, query_output = output, history=history_rev)


if __name__ == "__main__":
    app.run(debug=True)
    

