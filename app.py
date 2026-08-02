from flask import Flask, request
from flask import render_template
# from flask import url_for

import base64
import json


app = Flask(__name__)
# url_for('static', filename='style.css')

def check_cookie():
    cookie = request.cookies.get('info')
    if cookie:
        return cookie
    return False

@app.route("/")
def hello_world():
    name = request.cookies.get('name')
    username = request.cookies.get('username')
    branch = request.cookies.get('branch')

    if name and username and branch:
        return render_template('home.html', name = name, username=username, branch=branch)
    return render_template('index.html')

