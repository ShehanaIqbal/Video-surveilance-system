from flask import Flask,render_template
from forms import RegistrationForm,LoginForm

app=Flask(__name__)

app.config['SECRET_KEY']='f36c53ad14fea64f1c8f5526da7f2022'

posts=[
	{
		'author':'Nasar Hussain',
		'title':'Blog post 1',
		'content': 'First post content',
		'date_posted':'July 5,2018'
	},
	{
		'author':'Shehana Iqbal',
		'title':'Blog post 2',
		'content': 'Second post content',
		'date_posted':'December 20,2018'
	}
]

@app.route("/")
@app.route("/home")
def hello():
	return render_template('home.html',posts=posts)

@app.route("/about")
def about():
	return render_template('about.html',title="welcome")

@app.route("/register")
def register():
	form=RegistrationForm()
	return render_template('register.html',title="register",form=form)

@app.route("/login")
def login():
	form=LoginForm()
	return render_template('login.html',title="login",form=form)



if __name__=='__main__':
	app.run(debug=True)

