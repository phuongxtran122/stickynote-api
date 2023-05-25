import os
from flask import Flask, jsonify, request
from flask_cors import CORS
import check

app = Flask(__name__)
CORS(app)

@app.route("/")
def default():
    response = {
        'userID':3
    }
    return jsonify(response)

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    pwd = request.headers.get("API_KEY")
    if check.auth(pwd):
        return jsonify({"today": pwd})
    return jsonify({"today": pwd})

if __name__ == '__main__':
    app.run()