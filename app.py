# pytubefix Version 1.0

from flask import Flask, request, render_template, send_file
from pytube import YouTube
from downloader import downloadmp3, downloadPlaylist
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
@app.route("/home", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        url = request.form.get("url")  # Use .get() to safely access form data
        action = request.form.get("action") #Downloading one video or multiple videos
        if url:  # Check if the URL is not empty
            if action == "Convert":
                file_path = downloadmp3(url)
            elif action == "Download All":
                file_path = downloadPlaylist(url)
        else:
             return render_template("index.html", error="Please enter a valid URL")
        #return render_template("index.html")  # Re-render the template after processing
        return send_file(file_path, as_attachment=True)
    else:
        return render_template("index.html")

def showurl(url):
    print(f"User submitted URL: {url}")  # Prints the submitted URL in the console

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
