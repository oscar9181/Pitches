from flask import render_template, url_for, flash,redirect
from app import app,db,bcrypt
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post
from flask_login import login_user,current_user,logout_user,login_required



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
    if current_user.is_authenticated:
        return redirect(url_for('home'))  
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
    if current_user.is_authenticated:
        return redirect(url_for('home')) 
    form = LoginForm()
    if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password,form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('home'))
            else:
                flash('login unsuccessful.please check email and password','danger')
    return render_template('login.html',title='Login',form=form)
   
@app.route('/logout')
def logout():
    logout_user()
    
    return redirect(url_for('home'))
      
   
   
@app.route('/account')
@login_required
def account():
    
    return render_template('account.html',title='Account')
   


