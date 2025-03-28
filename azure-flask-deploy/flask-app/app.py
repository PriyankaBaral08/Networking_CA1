
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/dashboard', methods=['POST'])
def dashboard():
    username = request.form['username']
    return render_template('dashboard.html', username=username)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
