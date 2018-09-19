import os


SECRET_KEY = 'you-will-never-guess'

DEBUG = True

DB_USERNAME = 'root'
DB_PASSWORD = 'ahljljj'
BLOG_DATABASE_NAME = 'blog'
DB_HOST = os.getenv('IP', 'localhost')
DB_URL = 'mysql+pymysql://%s:%s@%s/%s' %(DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URL
SQLALCHEMY_TRACK_MODIFICATIONS = True