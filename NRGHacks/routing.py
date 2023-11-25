from flask import Flask, render_template, request, redirect, session

app = Flask(__name__, template_folder='templates')


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username-input']
    password = request.form['password-input']
    login = False
    if username == 'password' and password == 'hi':
        login = True

    return render_template("index.html", login=login)
    