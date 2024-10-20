from flask import Flask, request, url_for, render_template, request

app = Flask(__name__)


@app.route("/home",methods=["POST","GET"])
@app.route("/",methods=["POST","GET"])
def home():
     return render_template("index.html")
        

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80,debug=True)