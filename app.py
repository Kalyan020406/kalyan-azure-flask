from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Kalyan's Azure App Service! 🚀"