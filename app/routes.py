from flask import render_template,flash,redirect,url_for
from app import app
from app.forms import LoginForm,RegistrationForm
@app.route('/')
@app.route('/index')
def index():
	#return "Hello World";
	user={'username':'Ellee'}
	posts=[
		{
			'author':{'username':'Paul'},
			'body':'System Administration Fundamentals'
		},
		{	
			'author':{'username':'Jules'},
			'body':'The Fundamentals of Game Design and Development'
		},
		{	
			'author':{'username':'Rotherford'},
			'body':'The Concepts of Object Oriented Programming'
		},
		{	
			'author':{'username':'Nhoj'},
			'body':'The Art of Project Management'
		}

	]
	return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
    	flash("Login requested for user {} and password {}, remember_me={}".format(form.username.data, form.password.data, form.remember_me.data))
    	return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/register',methods=['GET','POST'])
def register():
	reg_form=RegistrationForm()
	if reg_form.validate_on_submit():
		print("Last Name: ", reg_form.last_name.data)
		print("First Name: ", reg_form.first_name.data)
		print("Email: ", reg_form.email.data)
		print("Username: ", reg_form.username.data)
		print("Password: ", reg_form.password.data)
		flash("You are registered now {} {}".format(reg_form.first_name.data, reg_form.last_name.data))
		return redirect('/index')
	return render_template('register.html', title='Register',reg_form=reg_form)
