#!/usr/bin/env python3
"""Module that implements the forms feature of the application
"""

from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms import SubmitField, StringField, PasswordField, BooleanField

class RegistrationForm(FlaskForm):
    """Class that handles the registration task for new users"""
    username = StringField("Username", validators=[DataRequired(),Length(min=2, max=20)])
    surname = StringField("Surname", validators=[DataRequired(),Length(min=2, max=20)])
    first_name=StringField("First_name", validators=[DataRequired(),Length(min=2, max=20)])
    other_name=StringField("Other_name", validators=[DataRequired(),Length(min=2, max=20)])
    email = StringField("Email", validators=[DataRequired(),Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(),EqualTo("password")])
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        """to validate the uername provided by user against database"""
    
    def validate_email(self, email):
        """module that validates email provded by new user against database"""

class Login(FlaskForm):
    """class that handles the login task of user"""
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember me")
    Submit = SubmitField("Login in")