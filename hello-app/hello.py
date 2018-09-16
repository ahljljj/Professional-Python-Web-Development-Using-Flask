from flask import Flask, url_for, request, render_template

import os

app = Flask(__name__)


@app.route('/login', methods = ['GET', "POST"])

def login():
    if request.method ==  'POST':
        return 'Username %s logged in' % request.form['username']
    return render_template('login.html')



@app.route('/login2', methods = ['GET','POST'])

def login2():
    if request.method == "POST":
        return "username " + request.values['username']
    else:
        return '<form method = "post" action = "/login"><input type = "text" name = "username" /><p><button type = "submit">Submit</button></form>'


@app.route('/hello/<name>')
def hello(name = None):
    return render_template('hello.html', name = name)


@app.route('/')

def index():
    return url_for('show_post_id', post_id = 4)

@app.route('/username/<username>')

def user_profile(username):
    return "user %s" %username

@app.route('/post/<int:post_id>')

def show_post_id(post_id):
    return "Post " + str(post_id)


@app.route('/hello')

def hello_world():
#    import pdb
#    pdb.set_trace()
#    i = 3
#    i = i + 1
#    visited = i
#    return "Hello Everyone!" + "You have visited " + str(visited) + " times."
     return "Hello World!"

if __name__ == '__main__':
    app.debug = True
    host = os.getenv('IP','0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.run(host = host, port = port)
