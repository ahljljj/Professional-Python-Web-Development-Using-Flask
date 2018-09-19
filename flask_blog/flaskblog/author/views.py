from flaskblog import app

@app.route('/login')

def login():
    return "Hello, User!"