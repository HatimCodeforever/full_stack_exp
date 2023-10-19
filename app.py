from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user
from flask_login.utils import login_required
app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SECRET_KEY"] = "abc"
db = SQLAlchemy(app)
login_manager = LoginManager(app)

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True,nullable=True)
    password = db.Column(db.String(250), nullable=False)

db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = Users(username=request.form.get('username'), password=request.form.get('password'))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = Users.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for("template"))
    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route('/',methods=['GET'])
def default():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>PARAGRAPH</h1>
    <p>A modern laptop is a portable computing device that combines the functionality of a desktop computer into a compact, lightweight form factor. Laptops come in various sizes, from ultraportable models with small screens to larger, more powerful machines designed for tasks like gaming or content creation. They typically feature a keyboard, touchpad or trackpad, and a built-in display. Laptops run on operating systems such as Windows, macOS, or Linux and are powered by processors from companies like Intel or AMD. With options for different storage capacities, memory sizes, and screen resolutions, laptops cater to a wide range of user needs, from everyday web browsing and office tasks to demanding graphics-intensive applications.</p>
    <img src="/static/product3.jpg" alt='LAPTOP' height=500 width=500></img>
    <br>
</body>
</html>
    FIRST PAGE
    I M SO EXCITED!!!
    <a href="http://127.0.0.1:5000/an"></a>
    """
@app.route('/an',methods=['GET'])
def home():
    return "Hello an !"
print('initiated the app with name of:',__name__)

@app.route('/hp')
def homepage():
    print("hey i m visitng the homepage!")
    return "HELLO HOMEPAGE"

@app.route('/user/<username>')
def show_user(username):
    return f'Hello {username}!'

@app.route('/post/<int:id>')
def show_post(id):
    return f'This post has the id {id}'

@app.route('/vstring/<name>')
def string(name):
    return 'This is a %s string' %name

@app.route('/vfloat/<float:no>')
def float(no):
    return 'My balance is %f' %no

@app.route('/template')
def template():
    return render_template('dashboard.html')


@app.route('/testingrequest',methods=['GET','POST'])
def squarepost():
    if request.method == "POST":
        name = request.form['name']
        course = request.form['course']
        return render_template('show.html',name=name,course=course)
        
    if request.method == 'GET':
        return render_template('show.html')


if (__name__=='__main__'):
    print("Server has Started")
    app.run(use_reloader=True,debug=True)