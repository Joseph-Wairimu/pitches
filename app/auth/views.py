from flask import render_template,request,redirect,url_for,abort

@auth.route('/login')
def login():

    '''
    View root page function that returns the index page and its data
    '''
    
    
    return render_template('login.html')    