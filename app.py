from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/<nameT>")
def home(nameT):
    return render_template("index.html",name=nameT)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)