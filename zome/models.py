#!/usr/bin/env python3

"""Script that outlines the data model of the application"""

from zome import db
from datetime import datetime
from flask_login import UserMixin


class User(db.Model, UserMixin):
    """class that decribes the data of users"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    profile_pics = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(65), nullable=False)
    phone_no = db.Column(db.String(15), nullable=False, unique=True)
    land_listing = db.relationship("Land_listing", backref="author", lazy=True)
    gender = db.Column(db.String(10), nullable=False)


    def __repr__(self):
        """method that provides string representation of User object"""
        return f"User('{self.username}', '{self.email}', '{self.profile_pics}')"

class Land_listing(db.Model):
    """class tha handles the data posted has land listing"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    size = db.Column(db.Float, nullale=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        """Method that provides string representaton of Land Listing object"""
        return f"Land Listing('{self.title}', '{self.price}', '{self.date_posted}')"
    
class House_listing(db.Model):
    """class that handles the data posted as house listing"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    size = db.Column(db.Float, nullale=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

class Admin(db.Model, UserMixin):
    """class that handles the admin proviedge data"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=True)
    password = db.Column(db.String(20), nullable=False)
    email=db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        """method that provides string representation for Admin Class"""
