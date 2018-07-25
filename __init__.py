from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Abdullah/Desktop/todo/todo.db'
db = SQLAlchemy(app)

import routes