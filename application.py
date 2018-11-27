from flask import Flask, render_template, request, redirect, url_for
from flask_session import Session

app = Flask("__name__")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Todo = []
username = None
@app.route("/", methods=["GET", "POST"])
def index():
    # if not username == None:
    #     return redirect(url_for('mylist', username=username, todo=Todo))
    # else:
    return render_template("index.html")

@app.route("/todo", methods=["GET", "POST"])
def todo():
    username = request.form.get("username")
    return render_template("todo.html", username=username)

@app.route("/mylist", methods=["GET", "POST"])
def mylist():
    if request.method == "POST":
        item = request.form.get("list")
        Todo.append(item)
    return render_template("todo.html", username=username, todo=Todo)
