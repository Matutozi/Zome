#!/usr/bin/env python3
"""Module that implements the forms feature of the application
"""

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms.validators import (
        DataRequired, Length, Email, EqualTo, ValidationError, Regexp
        )
from wtforms import SubmitField, StringField, PasswordField, BooleanField, TextAreaField, FloatField, IntegerField
from zome.models import User


class RegistrationForm(FlaskForm):
    """Class that handles the registration task for new users"""
    username = StringField(
            "Username",
            validators=[DataRequired(), Length(min=2, max=20)])
    surname = StringField(
        "Surname",
        validators=[DataRequired(), Length(min=2, max=20)])
    firstname = StringField(
        "First Name",
        validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    phone = StringField("Phone Number", validators=[Regexp('^\+(?:[0-9] ?){6,14}[0-9]$')])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
            "Confirm Password",
            validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        """to validate the uername provided by user against database"""
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("That username is taken, choose another one")

    def validate_email(self, email):
        """module that validates email provded by new user against database"""
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That email is taken, choose another one")


class Login(FlaskForm):
    """class that handles the login task of user"""
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember me")
    Submit = SubmitField("Login")


class UpdateForm(FlaskForm):
    """class that updates information"""
    username =  StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

class ListingForm(FlaskForm):
    """module that stores land listing data for storage in the database"""
    title = StringField('Title', validators=[DataRequired(), Length(min=5, max=100)],
            render_kw={'placeholder': "E.g. The King's Villa"})
    description = TextAreaField('Description', validators=[DataRequired()],
            render_kw={'placeholder': "Situated in the suburbs..."})
    price = FloatField('Price ($)', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    number_rooms = IntegerField('Number of Rooms', validators=[DataRequired()])
    number_bathrooms = IntegerField('Number of Bathrooms', validators=[DataRequired()])
    size = FloatField('Size (sqm)', validators=[DataRequired()])
    image = FileField('Upload Image', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Add Listing')

# class HouseListingForm(LandListingForm):
#     """module that stores house listing data and inherits from land listing form"""
#     number_rooms = IntegerField('Number of Rooms', validators=[DataRequired()])
#     number_bathrooms = IntegerField('Number of Bathrooms', validators=[DataRequired()])
