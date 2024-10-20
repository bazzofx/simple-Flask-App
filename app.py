from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
@app.route("/home", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        url = request.form.get("url")  # Use .get() to safely access form data
        if url:  # Check if the URL is not empty
            showurl(url)
        return render_template("index.html")  # Re-render the template after processing
    else:
        return render_template("index.html")

def showurl(url):
    print(f"User submitted URL: {url}")  # Prints the submitted URL in the console

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
