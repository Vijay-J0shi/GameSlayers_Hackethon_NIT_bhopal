from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,BooleanField,TextAreaField
from wtforms.validators import DataRequired,Length,EqualTo,Email,ValidationError,Regexp
from flashblog.models import *



class Partner_with_us_Form(FlaskForm):
    company_name=StringField("Company / Organization name",validators=[Length(min=5,max=30)])
    industry=StringField("Industry / Sector",validators=[Length(min=5,max=30)])
    contact_person_name=StringField("Contact Person's name",validators=[DataRequired()])
    position=StringField("Position / Title")
    email=StringField("Email Address",validators=[DataRequired(),Email()])
    phone=StringField("Phone number",validators=[DataRequired(),Length(min=10,max=10),Regexp('^[0-9]*$', message='Phone number must contain only numbers')])
    content=TextAreaField("Content",validators=[DataRequired(),Length(min=0,max=300)],render_kw={'rows': 6, 'cols': 80,'placeholder':'''Specific goals and objectives the organization aims to achieve through the partnership.
Also, do mention the areas of waste management or sustainability the organization is focused on.''' })
    integration=TextAreaField("Integration",validators=[Length(min=0,max=300)],render_kw={'rows': 6, 'cols': 80,'placeholder':'''How are you planning to integrate ECOSORT's technology into your operations.
Technical specifications or requirements for integration can be helpful for us to cater your expected result'''})
    submit=SubmitField("Submit")


    def validate_email(self, email):  # we can also check this in validate_on submit method also(but using different method)

            user = User.query.filter_by(email=email.data).first()
            if user: # check if user with given username already exist or not
                raise ValidationError('Email already registered.')

    def validate_phone(self, phone):
            user = User.query.filter_by(phone_number=phone.data).first()
            if user:
                raise ValidationError('Your Phone number is wrong ,check again')
