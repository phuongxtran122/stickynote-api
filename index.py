import os
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def default():
    return "Server is online..."

if __name__ == '__main__':
    app.run()