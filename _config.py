import os

# grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'data.db'

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)
