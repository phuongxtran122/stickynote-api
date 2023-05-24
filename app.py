import os
import requests
import json
import urllib.parse

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hi():
    return "This home"

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)