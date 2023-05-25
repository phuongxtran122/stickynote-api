import os
from flask import Flask, jsonify, request
from flask_cors import CORS
import check

app = Flask(__name__)
CORS(app)
number = 0
@app.route("/")
def default():
    global number
    number+=1
    response = {
        'userID':number
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