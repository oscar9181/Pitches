from flask import Flask,render_template
from app import app

@app.route('/')
@app.route('/home')
def home():

    '''
    View root page function that returns the home page and its data
    '''

    
    return render_template('home.html')
