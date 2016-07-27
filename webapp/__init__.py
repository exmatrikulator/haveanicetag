from flask import Flask
from flask_assets import Environment
from flask_sqlalchemy import SQLAlchemy
from webassets.loaders import PythonLoader as PythonAssetsLoader
import webapp.assets


app = Flask(__name__)
app.config.from_pyfile('../config.py')
db = SQLAlchemy(app)

assets_env = Environment(app)
assets_loader = PythonAssetsLoader(webapp.assets)
for name, bundle in assets_loader.load_bundles().items():
    assets_env.register(name, bundle)


#import app.forms
import webapp.views


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
