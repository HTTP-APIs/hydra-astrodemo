from flask import Flask,render_template,request
from hydra_redis import querying_mechanism
from hydra_redis import querying_mechanism

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/', methods= ['GET','POST'])
def enter_url():
    if request.method == 'GET':
        return render_template("index.html")
    if request.method == 'POST':
        if 'url' in request.form:
            url= request.form['url']
            handle_data = querying_mechanism.HandleData()
            global apidoc
            apidoc = handle_data.load_data(url)
            print(url,apidoc)
            return render_template("index.html", apidoc = apidoc)
        elif 'query' in request.form:
            query = request.form['query']
            print(query)
            return render_template("index.html",apidoc)

#@app.route('/', methods= ['GET','POST'])
#def enter_query():
#    if request.method == 'GET':
#        return render_template("index.html")
#    if request.method == 'POST':
#        query = request.form['query']
#        print(query)
#        return render_template("index.html")

if __name__ == "__main__":
    app.run()

