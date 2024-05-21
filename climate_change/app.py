from flask import Flask, render_template, request, redirect, url_for, flash, session
from forum_db import ForumDB
from ghg_db import GHG_DB
import password_util
import email_util
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some secret key'

_forum_db = ForumDB()
_ghg_db = GHG_DB()
_admin_code = '123' # given to super user by administrator

NOBODY_EMAIL = 'nobody@nobody'

@app.route('/')
def index():
    increment_web_page_visit_count('index.html')
    return render_template('index.html')

@app.route('/facts')
def facts():
    increment_web_page_visit_count('facts.html')
    return render_template('facts.html')

@app.route('/news')
def news():
    increment_web_page_visit_count('news.html')
    return render_template('news.html')

@app.route('/solutions')
def solutions():
    increment_web_page_visit_count('solutions.html')
    return render_template('solutions.html')

@app.route('/signup', methods=('GET', 'POST'))
def signup():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        # global _admin_code
        is_admin = 1 if request.form['admin_code'] == _admin_code else 0
        if not email or not password:
            if not email:
                flash('Email is required')
            if not password:
                flash('Password is required')
        else:
            user = _forum_db.select_user(email)
            if user:
                flash('Account exists.  Sign in?')
            else:
                salt, password_hash = password_util.hash_new_password(password)
                _forum_db.create_user(first_name, last_name, email, salt, password_hash, is_admin)
                return redirect(url_for('signin'))

    increment_web_page_visit_count('signup.html')
    return render_template('signup.html')

@app.route('/signin', methods=('GET', 'POST'))
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if not email or not password:
            if not email:
                flash('Email is required')
            if not password:
                flash('Password is required')
        else:
            user = _forum_db.select_user(email)
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
                        session['signed_in'] = True
                        session['is_admin'] = user['is_admin'] == 1
                        session['email'] = user['email']
                        return redirect(url_for('index'))

    increment_web_page_visit_count('signin.html')
    return render_template('signin.html')

@app.route('/signout', methods=('GET',))
def signout():
    session['signed_in'] = False
    session['is_admin'] = False
    session['email'] = NOBODY_EMAIL
    increment_web_page_visit_count('index.html')
    return render_template('index.html')

@app.route('/forgot_password_1', methods=('GET', 'POST'))
def forgot_password_1():
    if request.method == 'POST':
        email = request.form['email']
        user = _forum_db.select_user(email)
        if not user:
            flash("'" + email + "' not found")
            return render_template('forgot_password_1.html')
        token = uuid.uuid4().hex
        session['token'] = token
        email_util.send(email, token)
        message = 'Please follow email instruction (at ' + email  + ') to get the temporary password.'
        flash(message)
        return redirect(url_for('forgot_password_2', email=email))
    return render_template('forgot_password_1.html')

@app.route('/forgot_password_2', methods=('GET', 'POST'))
def forgot_password_2():
    if request.method == 'POST':
        email = request.args.get('email')
        temp_password = request.form['temp_password']
        if temp_password != session['token']:
            message = 'Please follow email instruction (at ' + email  + ') to get the temporary password.'
            flash(message)
            return render_template('forgot_password_2.html', email=email)
        return redirect(url_for('reset_password', email=email))
    return render_template('forgot_password_2.html')

@app.route('/reset_password', methods=('GET', 'POST'))
def reset_password():
    if request.method == 'POST':
        email = request.args.get('email')
        password = request.form['password']
        repeat_password = request.form['repeat_password']
        if password != repeat_password:
            flash("Password and Repeat Password must be same.")
            return render_template('reset_password.html', email=email)
        user = _forum_db.select_user(email)
        salt = user['salt']
        new_password_hash = password_util.hash_password(password, salt)
        _forum_db.update_password(email, new_password_hash)
        return redirect(url_for('signin'))
    return render_template('reset_password.html')

@app.route('/forum', methods=('GET',))
def forum():
    forums = _forum_db.get_all_forums()
    comments = _forum_db.get_all_comments()
    users = _forum_db.get_all_users()
    increment_web_page_visit_count('forum.html')
    return render_template('forum.html', forums=forums, comments=comments, users=users, find_comments_by_forum_id=find_comments_by_forum_id, find_user_by_email=find_user_by_email)

def find_comments_by_forum_id(forum, all_comments):
    forum_comments = list()
    for comment in all_comments:
        if comment['forum_id'] == forum['id']:
            forum_comments.append(comment)
    return forum_comments

def find_user_by_email(users, email):
    for user in users:
        if user['email'] == email:
            return user
    return None

@app.route('/forum/create_forum', methods=('GET', 'POST'))
def create_forum():
    if request.method == 'POST':
        topic = request.form['topic']
        user_email = session['email']
        if not topic:
            flash('Topic is required')
        else:
            _forum_db.create_forum(topic, user_email)
            return redirect(url_for('forum'))
    increment_web_page_visit_count('create_forum.html')
    return render_template('create_forum.html')

@app.route('/forum/<int:forum_id>/create_comment', methods=('GET', 'POST'))
def create_comment(forum_id):
    if request.method == 'POST':
        comment = request.form['comment']
        user_email = session['email']
        if not comment:
            flash('Comment is required')
        else:
            _forum_db.create_comment(comment, forum_id, user_email)
            return redirect(url_for('forum'))
    increment_web_page_visit_count('create_comment.html')
    return render_template('create_comment.html')

# DELETE / PUT can't be used as only GET / POST are supported - use POST instead
# https://stackoverflow.com/questions/5162960/should-put-and-delete-be-used-in-forms
# @app.route('/forum/<int:forum_id>/delete_forum', methods=('DELETE',))
@app.route('/forum/<int:forum_id>/delete_forum', methods=('POST',))
def delete_forum(forum_id):
    _forum_db.delete_forum(forum_id)
    return redirect(url_for('forum'))

# DELETE / PUT can't be used as only GET / POST are supported - use POST instead
# https://stackoverflow.com/questions/5162960/should-put-and-delete-be-used-in-forms
# @app.route('/forum/<int:comment_id>/delete_comment', methods=('DELETE',))
@app.route('/forum/<int:comment_id>/delete_comment', methods=('POST',))
def delete_comment(comment_id):
    _forum_db.delete_comment(comment_id)
    return redirect(url_for('forum'))

@app.route('/visit_count', methods=('GET',))
def visit_count():
    visit_report = _forum_db.get_web_site_visit_count()
    increment_web_page_visit_count('visit_count')
    return render_template('visit_count.html', visit_report=visit_report)

def increment_web_page_visit_count(web_page):
    user_email = session['email'] if 'email' in session.keys() else NOBODY_EMAIL
    _forum_db.increment_web_page_visit_count(web_page, user_email)
