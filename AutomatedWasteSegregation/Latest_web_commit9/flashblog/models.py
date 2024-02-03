
from flashblog import db
from flask_login import LoginManager,UserMixin
from flashblog import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    company=db.Column(db.String(40),default="XYZ company")
    industry= db.Column(db.String(30), default="YYY industry")
    contact_name = db.Column(db.String(40))
    position = db.Column(db.String(30), default="zzz")
    email = db.Column(db.String(30), unique=True,nullable=False)
    phone_number=db.Column(db.Integer,  unique=True,nullable=False)
    objective=db.Column(db.String(300),default="None")
    integration=db.Column(db.String(300),default="None")

    def __repr__(self):
        return f"User('{self.contact_name}', '{self.email}', '{self.industry}')"


class Personal_Info(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    contact_name = db.Column(db.String(40))
    email = db.Column(db.String(30), unique=True,nullable=False)
    phone_number=db.Column(db.Integer, unique=True,nullable=False)
    skills=db.Column(db.String(300),default="None")


    def __repr__(self):
        return f"User('{self.phone_number}', '{self.email}', '{self.contact_name}')"