from flask import Flask,render_template,request
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("form.html")
"""
def index():
    now=datetime.datetime.now()
    new_year=now.month==1 and now.month==2
    return render_template("index.html",new_year=new_year)
"""
@app.route('/more')
def names():
    names=['Alice','Bob','Charlie']
    return render_template("index1.html",names=names)

@app.route("/<string:name1>")
def hellos(name1):
    return f"Hello ,{name1}!"

@app.route('/bye')
def bye():
    headline="Goodbye"
    return render_template("index.html",headline=headline)

#rendering between 2 pages . index3.html->index2.html->index3.html
@app.route("/index3")
def interview():
    return render_template("index3.html")

@app.route("/index2")
def index2():
    return render_template("index2.html")
#common layout.html
@app.route("/first")
def first():
    return render_template("more.html")

@app.route("/second")
def second():
    return render_template("second.html")

#form
@app.route("/hello",methods=["POST"])
def hello():
    name=request.form.get("name")
    return render_template("output.html",name=name)

app.run('127.0.0.1', debug=True)

"""
>>> import socket
>>> socket.getaddrinfo('localhost', 8080)
[(<AddressFamily.AF_INET6: 23>, 0, 0, '', ('::1', 8080, 0, 0)), (<AddressFamily.AF_INET: 2>, 0, 0, '', ('127.0.0.1', 8080))]

"""