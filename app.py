from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/faq.html")
def FAQ():
    return render_template("faq.html")

@app.route("/login.html",methods=["GET","POST"])
def login():
    if request.method =="POST":
        user = request.form["url"]
        return redirect(url_for("user",usr=user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80,debug=True)

