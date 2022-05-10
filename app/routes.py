from flask import render_template, url_for, flash, redirect
from app.forms import RegistrationForm, LoginForm
from app import app,db,bcrypt
from app.models import User, Post


pitches = [
   {
    'author' :'Sophie Paxton',
    'title'  :'Interface Design',
    'pitch'  :'Animation is like cursing. If you overuse it, it loses all its impact.',
    'date_posted' : 'October 17 2002'
   },
   {
    'author' :'Jessica Cherner',
    'title'  :'Architectural Design.',
    'pitch'  :'On the famed Billionaire Row, SHoP Architects and Studio Sofield have delivered on a long-awaited promise',
    'date_posted' :'April 11 2022'
   },
   {      
    'author' :'Jeff Bezos',
    'title'  :'Forbes',
    'pitch'  :'I have not failed. I have just found 10,000 ways that wil not work.',
    'date_posted' :'May 11 2008'
   },
   {
    'author' :'Oscar',
    'title'  :'Advertisement',
    'pitch'  :'A walk in the moon book ',
    'date_posted' :'March 13 2010'
     }
    ]


@app.route('/')
@app.route('/home')
def home():    
    '''
    View root page function that returns the home page and its data
    '''
    return render_template('home.html',pitches=pitches)


@app.route('/about')
def about():
        return render_template('about.html')
    


@app.route('/register',methods=['GET','POST'])
def register():  
    form = RegistrationForm()
    if form. validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user= User(username=form.username.data, email=form.email.data,password=hashed_password)  
        db.session.add(user)
        db.session.commit()
        flash('Your account hass been created!','success')
        return redirect(url_for('Login'))
    return render_template('register.html',title='Register',form=form)

@app.route('/login',methods=['GET','POST']) 
def Login():  
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'oscar@okolla.com' and form.password.data == 'abcdef':
            flash('You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash('login unsuccessful.please check email and password','danger')
    return render_template('login.html',title='Login',form=form)
   
