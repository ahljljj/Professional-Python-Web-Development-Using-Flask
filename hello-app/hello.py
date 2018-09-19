from flask import Flask, url_for, request, render_template, redirect, flash, make_response, session

import os
import pymysql

app = Flask(__name__)


import logging
from logging.handlers import RotatingFileHandler

@app.route('/login', methods = ['GET', "POST"])

def login():
    error = None
    if request.method ==  'POST':
#        return 'Username %s logged in' % request.form['username']
         if valid_login(request.form['username'], request.form['password']):
#             return 'Welcome back, %s' % request.form['username']
             flash('Successfully logged in')
             session['username'] = request.form.get('username')
             return redirect(url_for('welcome'))
         else:
              error = 'Incorrect username or password'
              app.logger.warning("Incorrect username and password for user (%s)" % request.form.get("username"))
    return render_template('login.html', error = error)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

def valid_login(username, password):
#    if username == password:
     # mysql
     mysql_database_host = os.getenv('IP','localhost')
     mysql_database_user = 'root'
     mysql_database_password = 'ahljljj'
     mysql_database_db = 'my_flask_app'
     conn = pymysql.connect(host = mysql_database_host,
                            user = mysql_database_user,
                            passwd = mysql_database_password,
                            db = mysql_database_db)
     cursor = conn.cursor()
     cursor.execute("SELECT * FROM user WHERE username = '%s' ANd password = '%s'" % (username, password))
     data = cursor.fetchone()
     if data:
        return True
     else:
        return False


@app.route('/')

def welcome():
    if 'username' in session:
        return render_template('welcome.html', username = session['username'])
    else:
        return  redirect(url_for('login'))



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
    app.secret_key = "hc\x19\x12\x10\xac\xd3+C\x1e\xc8+\xa2O\xbb\xdf\xbe\xa2;\xe2\x1c\x92\xae\xd0"

    #logging
    handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount= 1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)

    app.run(host = host, port = port)

