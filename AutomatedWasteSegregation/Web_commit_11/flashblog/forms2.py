from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,BooleanField,TextAreaField
from wtforms.validators import DataRequired,Length,EqualTo,Email,ValidationError,Regexp
from flashblog.models import *

class Collaborate_with_us_Form(FlaskForm):
   
    full_name=StringField("Full Name",validators=[Length(min=5,max=30),DataRequired()])
    email=StringField("Email",validators=[DataRequired(),Email()])
    phone=StringField("Phone number",validators=[DataRequired(),Length(min=10,max=10),Regexp('^[0-9]*$', message='Phone number must contain only numbers')])
    content=TextAreaField("Content",validators=[DataRequired(),Length(min=0,max=300)],render_kw={'rows': 4, 'cols': 50,'placeholder':'''Relevant skills or expertise that you will be
    bringing in during collaboration.'''
 })
    submit=SubmitField("Submit")

    
    def validate_email(self, email):  # we can also check this in validate_on submit method also(but using different method)

            user = Personal_Info.query.filter_by(email=email.data).first()
            if user: # check if user with given username already exist or not
                raise ValidationError('Email already registered.')

    def validate_phone(self, phone):
            user = Personal_Info.query.filter_by(phone_number=phone.data).first()
            if user:
                raise ValidationError('Your Phone number is wrong ,check again')



