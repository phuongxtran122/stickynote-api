import os
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def default():
    return "Server is online..."

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return os.APi_KEY

if __name__ == '__main__':
    app.run()