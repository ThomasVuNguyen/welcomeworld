from flask import Flask, redirect, url_for, render_template,request, Session
from flask_sqlalchemy import SQLAlchemy


app= Flask(__name__)
db = SQLAlchemy(app)


class nums(db.Model):
    _id = db.Column("id", db.Integer, primary_key = True)
    a = db.Column("a", db.String(100))
    b = db.Column("b", db.String(100))
    def __init__(self, name, email):
        self.a = a
        self.b = b


@app.route("/cal", methods = ["GET","POST"])
def cal():
    return render_template("calculator.html", title = "Tung is here")
    a = "a"
@app.route("/<a>")
def out(a):
    return render_template("out.html", a = 100, title= "ok")

if __name__=="__main__":
    app.run(debug=True)
