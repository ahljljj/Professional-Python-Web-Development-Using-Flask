from flaskblog import app
from flask import render_template, redirect, flash, url_for, session, abort
from blog.form import SetupForm, PostForm
from flaskblog import db
from author.models import Author
from blog.models import Blog
from author.decorators import login_required, author_required
import bcrypt

@app.route('/')
@app.route('/index')

def index():
    blogs = Blog.query.count()
    if blogs == 0:
        return redirect(url_for('setup'))
    return "Hello World!"

@app.route('/admin')
@login_required
@author_required

def admin():
    if session.get('is_author'):
        return render_template('blog/admin.html')
    else:
        abort(403)

@app.route('/setup', methods = ('GET', 'POST'))

def setup():
    form = SetupForm()
    error = ""

    if form.validate_on_submit():
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(form.password.data, salt)
        author = Author(
            form.fullname.data,
            form.email.data,
            form.username.data,
            hashed_password,
            True
        )
        db.session.add(author)
        db.session.flush()
        if author.id:
            blog = Blog(
                form.name.data,
                author.id
            )
            db.session.add(blog)
            db.session.flush()
        else:
            db.session.rollback()
            error = "Error creating user"
        if author.id and blog.id:
            db.session.commit()
            flash("Blog created")
            return  redirect(url_for('admin'))
        else:
            db.session.rollback()
            error = "Error creating blog"
    return render_template('blog/setup.html', form=form, error=error)

@app.route('/post', methods=('GET','POST'))
@login_required
@author_required
def post():
    form = PostForm()
    return render_template('blog/post.html', form=form)

@app.route('/article')
def article():
    return render_template('blog/article.html')



