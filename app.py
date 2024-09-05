from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/main.html')
def main():
    return render_template('main.html')

@app.route('/pages-faq.html')
def pages_faq():
    return render_template('pages-faq.html')

@app.route('/pages-register.html')
def pages_register():
    return render_template('pages-register.html')

@app.route('/pages-contact.html')
def contacto():
    return render_template('pages-contact.html')

@app.route('/pages-error-404.html')
def Error404():
    return render_template('pages-error-404.html')

@app.route('/users-profile.html')
def user_perfil():
    return render_template('users-profile.html')

@app.route('/pages-blank.html')
def blank():
    return render_template('pages-blank.html')

@app.route('/pages-login.html')
def login():
    return render_template('pages-login.html')