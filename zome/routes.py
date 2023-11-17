#!/usr/bin/env python3

"""Script that handles the flask routes for the application"""

from zome import app
from flask import render_template, redirect, url_for


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
def register():
    """route that handles registration of new users"""
    return render_template("register.html", title="Register")

@app.route("/login", methods=["GETS", "POSTS"])
def login():
    """route that handles login of authtnticated users"""
    return render_template("login", title="login")

@app.route("/logout")
def logout():
    """route that handles logout of users"""
    return redirect(url_for("home"))



