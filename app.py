from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "CI/CD with Docker using GitHub Actions!"
