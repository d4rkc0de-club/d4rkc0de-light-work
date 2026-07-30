from flask import Flask
from flask import render_template
# from flask import url_for

app = Flask(__name__)
# url_for('static', filename='style.css')

@app.route("/")
def hello_world():
    return render_template('index.html')

