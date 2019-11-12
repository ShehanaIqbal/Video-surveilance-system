from flask import Flask, render_template
from forms import RegistrationForm, LoginForm, AddmemberForm
# ----------------------------------------
from flask import Flask, render_template, request
from flask_mysqldb import MySQL


app = Flask(__name__)
# ---------------------------------------
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'softwarep'

mysql = MySQL(app)

app.config['SECRET_KEY'] = 'f36c53ad14fea64f1c8f5526da7f2022'

posts = [
    {
        'author': 'Nasar Hussain',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'July 5,2018'
    },
    {
        'author': 'Shehana Iqbal',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'December 20,2018'
    }
]
# -------------------------------------
@app.route('/register', methods=['POST'])
def register1():
	if request.method == "POST":
	
		form =RegistrationForm()
		username = form.username.data
		email = form.email.data
		password = form.password.data
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO User_table(username, email, password) VALUES (%s, %s, %s)",(username, email, password))
		mysql.connection.commit()
		cur.close()
		return 'success'
	return render_template('register.html')
# -------------------------------------------

@app.route('/addmember', methods=['POST'])
def addmember1():
	if request.method == "POST":
		form = AddmemberForm()
		name = form.name.data
		phone = form.phone.data
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO Family_members(name, phone) VALUES (%s, %s)",(name, phone))
		mysql.connection.commit()
		return 'Success'
	return render_template('addmember.html')


@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title="welcome")


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title="register", form=form)
	
@app.route("/addmember")
def addmember():
    form = AddmemberForm()
    return render_template('addmember.html', title="addmember", form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title="login", form=form)


if __name__ == '__main__':
    app.run(debug=True)
