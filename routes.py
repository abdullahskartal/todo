from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy
from __init__ import app, db
from model import Todo

@app.route("/")
def index():
    todos = Todo.query.all()
    return render_template("index.html",todos = todos)

@app.route("/add",methods = ["POST"])
def add():
    title = request.form.get("title")
    newTodo = Todo(title=title,completed= False)
    db.session.add(newTodo)
    db.session.commit()
    return redirect (url_for("index"))

@app.route("/complete/<string:id>")
def complete(id):
    todo = Todo.query.filter_by(id = int(id)).first()
    todo.completed = not todo.completed
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<string:id>")
def delete(id):
    todo = Todo.query.filter_by(id = id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))
    