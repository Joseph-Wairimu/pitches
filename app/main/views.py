from flask import render_template,request,redirect,url_for,abort

from flask_login import login_required, current_user
from . import main
@main.route('/')
def index():
    return render_template('index.html')

# @main.route('/profile')
# def profile():

#     '''
#     View root page function that returns the index page and its data
#     '''
    
    
#     return render_template('profile/profile.html')    



@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    '''
    View root page function that returns the index page and its data
    '''
    
    
    return render_template('profile/profile.html',user = user)    

