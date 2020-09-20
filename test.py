from flask import Flask, render_template, redirect,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("test1.html")
@app.route("/vnd")
def vnd():
    return render_template("test2.html")
if __name__=="__main__":
    app.run(debug = True)
