from email.policy import default
from flask import Flask, render_template,url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, column

from forms import  RegistrationForm,LoginForm

app =Flask(__name__)
app.config['SECRET_KEY'] = 'ac4d969b60'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite///:site.db'
db = SQLAlchemy(app)

class User(db.model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20), unique=True,nullable=False)
    email = db.Column(db.String(100), unique=True,nullable=False)
    image_file = db.Column(db.String(20),nullable=False,default='default.jpg')
    password =  db.Column(db.String(70),nullable=False)

def __repr__(self):
    return f"User('{self.username}','{self.email}','{self.image_file}')"

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
         flash(f'Account created for {form.username.data}!','success')
         return redirect(url_for('home'))
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
   



if __name__ == '__main__':
       app.run()
