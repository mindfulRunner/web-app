from flask import Flask, render_template, request, redirect, url_for, flash
from db import DB
import password_util

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some secret key'

_db = None

@app.route('/')
def index():
    init_db()
    return render_template('index.html')

@app.route('/signup', methods=('GET', 'POST'))
def signup():
    init_db()
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if not email or not password:
            if not email:
                flash('Email is required')
            if not password:
                flash('Password is required')
        else:
            user = _db.select_user(email)
            if user:
                flash('Account exists.  Sign in?')
            else:
                salt, password_hash = password_util.hash_new_password(password)
                _db.create_user(email, salt, password_hash)
                return redirect(url_for('signin'))

    return render_template('signup.html')

@app.route('/signin', methods=('GET', 'POST'))
def signin():
    init_db()
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if not email or not password:
            if not email:
                flash('Email is required')
            if not password:
                flash('Password is required')
        else:
            user = _db.select_user(email)
            if not user:
                flash('Account does not exist.  Sign up?')
            else:
                if not password:
                    flash('Password is required')
                else:
                    salt = user['salt']
                    stored_password_hash = user['password_hash']
                    is_correct_password = password_util.check_password(
                        salt,
                        stored_password_hash,
                        password
                    )
                    if not is_correct_password:
                        flash('Wrong email or password, try again')
                    else:
                        return redirect(url_for('index'))

    return render_template('signin.html')

def init_db():
    global _db
    if not _db:
        _db = DB()

#