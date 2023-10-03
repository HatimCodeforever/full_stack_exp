from flask import Flask,render_template,request
app=Flask(__name__)
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