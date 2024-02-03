from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
  
app.config["SECRET_KEY"]="71f2c6064865ab99174ff51bb843d218"
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///site.db"

db=SQLAlchemy(app)

login_manager=LoginManager(app)

from flashblog import routes