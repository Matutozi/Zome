#!/usr/bin/env python3

"""Script that outlines the data model of the application"""

import os
import secrets
from PIL import Image
from zome import db, login_manager, app
from datetime import datetime
from flask_login import UserMixin
import uuid

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Listing:
    "Represents the base model"
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    size = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(100), default="images/zome_placeholder-2.jpg")
    date_posted = db.Column(
            db.DateTime,
            nullable=False,
            default=datetime.utcnow)

    def to_dict(self):
        """Return info of class a dictionary"""
        attribs = self.__dict__.copy()
        attribs["__class__"] = type(self).__name__

        return attribs
    
    @staticmethod
    def save_picture(form_picture):
        random_hex = secrets.token_hex(8)
        _, f_ext = os.path.splitext(form_picture.filename)
        picture_fn = random_hex + f_ext
        picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

        output_size = (125, 125)
        i = Image.open(form_picture)
        i.thumbnail(output_size)
        i.save(picture_path)

        return picture_fn   


class User(db.Model, UserMixin):
    """class that decribes the data of users"""
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    username = db.Column(db.String(20), unique=True, nullable=False)
    surname = db.Column(db.String(30), unique=True, nullable=False)
    first_name = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    profile_pics = db.Column(
            db.String(20),
            nullable=False,
            default="default.jpg")
    password = db.Column(db.String(65), nullable=False)
    phone = db.Column(db.String(15), nullable=False, unique=True)
    land_listings = db.relationship("LandListing", backref="user", lazy=True)
    home_lisitings = db.relationship("HouseListing", backref="user", lazy=True)

    def __repr__(self):
        """method that provides string representation of User object"""
        return "User('{}', '{}', '{}')".format(
                self.username,
                self.email,
                self.profile_pics
                )


class LandListing(db.Model, Listing):
    """class tha handles the data posted has land listing"""
    user = db.Column(db.String(36), db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        """Method that provides string representaton of Land Listing object"""
        return "Land Listing('{}', '{}', '{}')".foemat(
            self.title,
            self.price,
            self.date_posted
        )


class HouseListing(db.Model, Listing):
    """class that handles the data posted as house listing"""
    number_rooms = db.Column(db.Integer, nullable=False, default=0)
    number_bathrooms = db.Column(db.Integer, nullable=False, default=0)
    user = db.Column(db.String(36), db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        """Method that provides string representaton of House Listing object"""
        return "House Listing('{}', '{}', '{}')".format(
            self.title,
            self.price,
            self.date_posted
        )


class Admin(db.Model):
    """class that handles the admin proviedge data"""
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    username = db.Column(db.String(20), unique=True, nullable=True)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
