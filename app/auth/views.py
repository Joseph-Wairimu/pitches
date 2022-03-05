from flask import render_template,redirect,url_for
from . import auth
@auth.route('/login')
def login():

    '''
    View root page function that returns the index page and its data
    '''
    
    
    return render_template('auth/login.html')    

@auth.route('/signup')
def signup():

    '''
    View root page function that returns the index page and its data
    '''
    
    
    return render_template('auth/signup.html')        

@auth.route('/logout')
def logout():

    '''
    View root page function that returns the index page and its data
    '''
    
    
    return redirect(url_for("main.index"))        