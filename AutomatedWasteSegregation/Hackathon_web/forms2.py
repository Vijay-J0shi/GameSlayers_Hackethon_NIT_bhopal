from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,BooleanField,TextAreaField
from wtforms.validators import DataRequired,Length,EqualTo,Email,ValidationError,Regexp



class Collaborate_with_us_Form(FlaskForm):
   
    full_name=StringField("Full Name",validators=[Length(min=5,max=30),DataRequired()])
    email=StringField("Email",validators=[DataRequired(),Email()])
    phone=StringField("Phone number",validators=[DataRequired(),Length(min=10,max=10),Regexp('^[0-9]*$', message='Phone number must contain only numbers')])
    content=TextAreaField("Content",validators=[DataRequired()],render_kw={'rows': 4, 'cols': 50,'placeholder':'''Relevant skills or expertise that you will be
    bringing in during collaboration.'''
 })
    submit=SubmitField("Submit")



