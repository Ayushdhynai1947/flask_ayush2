from flask import Blueprint,render_template

auth = Blueprint('auth',__name__)

@auth.route('/signup')
def signup():
    return "this page will be used to sign up users"


@auth.route('/login')
def login():
    return " this page is used for login in user"

@auth.route('/logout')
def logout():
    return "use this to log out"