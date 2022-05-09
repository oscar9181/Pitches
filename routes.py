from crypt import methods
from flask import Flask, render_template,url_for,flash,redirect
from forms import  RegistrationForm,LoginForm

app =Flask(__name__)

app.config['SECRET_KEY'] = 'ac4d969b60'

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

@app.route('/login')
def Login():  
    form = LoginForm()
    return render_template('login.html',title='Login',form=form)
   



if __name__ == '__main__':
       app.run()
