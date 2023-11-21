#!/usr/bin/env python3

"""Script that handles the flask routes for the application"""

from zome import app
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, current_user
from zome import bcrypt, db
from zome.models import User, LandListing, House_listing
from zome.models import Admin
from zome.forms import Login, RegistrationForm


@app.route("/")
@app.route("/home")
def home():
    """home route"""
    return render_template("home.html")


@app.route("/about")
def about():
    """about route"""
    return render_template("about.html")


@app.route("/register", methods=["GET", "POSTS"])
def user_register():
    """route that handles registration of new users"""
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        if bcrypt.check_password_hash(hashed_password, form.confirm_password.data):
            user = User(username=form.username.data, surname=form.surname.data,first_name=form.first_name.data,other_name=form.other_name.data,email=form.email.data, password=hashed_password)
            db.session.add(user)
            db.session.commit()

            flash("Account has been created", "success")
            return redirect(url_for("login"))
    
    else:
        flash("Password and confim password mismatch", "danger")

    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GETS", "POSTS"])
def login():
    """route   that handles login of authtnticated users"""
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    
    form = Login()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        admin = Admin.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("home"))
        
        elif admin and bcrypt.check_password_hash(admin.password, form.password.data):
            login_user(admin, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("home"))
        
        else:
            flash("Login not successful. Please enter valid credentials", "danger")
    
    return render_template("login.html", title='Login', form=form)
    


    return render_template("login", title="login")


@app.route("/logout")
def logout():
    """route that handles logout of users"""
    return redirect(url_for("home"))
