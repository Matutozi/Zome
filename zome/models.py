#!/usr/bin/env python3

"""Script that outlines the data model of the application"""

from zome import db

class User(db.Model):
    """class that decribes the data of users"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    profile_pics = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(65), nullable=False)
    land_listing = db.relationship("Land_listing", backref="author", lazy=True)

    def __repr__(self):
        """method that provides string representation of User object"""
        return f"User('{self.username}', '{self.email}', '{self.profile_pics}')"

class Land_listing(db.Model):
    """class tha handles the data posted has land listing"""

class house_listing(db.Model):
    """class that handles the data posted as house listing"""