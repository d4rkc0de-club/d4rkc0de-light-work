from flask import Flask, request, jsonify
from flask import render_template
# from flask import url_for
import sqlite3

import base64


app = Flask(__name__)
DB_FILE = "database.db"
# url_for('static', filename='style.css')

def check_cookie():
    cookie = request.cookies.get('info')
    if cookie:
        return cookie
    return False

def init_db():
    """Creates the database and tables if they do not exist yet."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            name TEXT NOT NULL,
            username TEXT PRIMARY KEY NOT NULL,
            branch TEXT NOT NULL,
            experience TEXT NOT NULL,
            device TEXT NOT NULL,
            logintime TEXT NOT NULL,
            lvl1flag TEXT,
            lvl1time TEXT,
            lvl2flag TEXT,
            lvl2time TEXT,
            lvl3flag TEXT,
            lvl3time TEXT,
            lvl4flag TEXT,
            lvl4time TEXT,
            totaltime TEXT
        )
    ''')
    conn.commit()
    conn.close()

# init_db()
def check_db(key, column):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    # this is vulnerable.
    # cursor.execute("INSERT INTO students VALUES ('John Doe', 'johndoe12', 'CS', 'Beginner', 'MacBook', '16:00', 'DONE', '16:15', 'DONE', '16:30', 'DONE', '16:45', 'DONE', '17:00', '01:00')")
    cursor.execute(f"SELECT 1 FROM students WHERE {column} = '{key}'")
    result = cursor.fetchone()
    return result

# print(check_db("johndoe12", "username"))

@app.route("/")
def home():
    name = request.cookies.get('name')
    username = request.cookies.get('username')
    branch = request.cookies.get('branch')
    # storing password in database
    if check_db(username, 'username'):
        return render_template('home.html', name = name, username=username, branch=branch)
    return render_template('index.html')


@app.route("/leaderboards")
def leaderboards():
    return render_template('leaderboards.html')


@app.route('/write', methods=['POST'])
def sq_write():
    return "hi"


@app.route('/validate', methods=['POST'])
def checker():
    return "hi"