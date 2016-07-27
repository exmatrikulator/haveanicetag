from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('../config.py')
db = SQLAlchemy(app)

#import app.forms
import webapp.views


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
