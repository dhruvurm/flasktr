import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktr.db'
USERNAME = 'dhruvurm'
PASSWORD = 'pass'
WTF_CSRF_ENABLED = True
SECRET_KEY = '1234'
DATABASE_PATH = os.path.join(basedir, DATABASE)
