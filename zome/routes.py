#!/usr/bin/env python3

"""Script that handles the flask routes for the application"""

from zome import app
from flask import render_template, redirect, url_for, request, flash, abort
from flask_login import login_user, current_user, logout_user, login_required
from zome import bcrypt, db
from zome.models import User, LandListing, HouseListing
from zome.models import Admin
from zome.forms import Login, RegistrationForm, UpdateForm
from zome.models import Listing


@app.route("/")
def home():
    """home route"""
    all_listings = [listing.to_dict() for listing in LandListing.query.all()]
    all_listings += [listing.to_dict() for listing in HouseListing.query.all()]
    return render_template("index.html", all_listings=all_listings)


@app.route("/about")
def about():
    """about route"""
    return render_template("about.html", title="About")


@app.route("/homes")
def homes():
    """homes route"""
    home_listings = [listing.to_dict() for listing in HouseListing.query.all()]
    print(home_listings[0])
    return render_template("homes_or_lands.html", home_listings=home_listings)

@app.route("/lands")
def lands():
    """lands route"""
    land_listings = [listing.to_dict() for listing in LandListing.query.all()]
    return render_template("homes_or_lands.html", land_listings=land_listings)

@app.route("/contact")
def contact():
    """contact route"""
    return render_template("contact.html", title="Contact Us")

@app.route("/register", methods=["GET", "POST"])
def user_register():
    """route that handles registration of new users"""
    if current_user.is_authenticated():
        return redirect(url_for("home"))
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)\
            .decode("utf-8")
        if bcrypt.check_password_hash(hashed_password,
                                      form.confirm_password.data):
            user = User(username=form.username.data,
                        surname=form.surname.data,
                        first_name=form.first_name.data,
                        email=form.email.data,
                        phone=form.phone.data,
                        password=hashed_password)
            db.session.add(user)
            db.session.commit()

            flash("Account has been created", "success")
            return redirect(url_for("login"))

    else:
        flash("Password and confim password mismatch", "danger")

    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    """route   that handles login of authtnticated users"""
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    form = Login()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        admin = Admin.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password,
                                               form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            if next_page:
                return redirect(next_page)
            else:
                redirect(url_for("home"))

        elif admin and bcrypt.check_password_hash(admin.password,
                                                  form.password.data):
            login_user(admin, remember=form.remember.data)
            next_page = request.args.get("next")
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for("home"))

        else:
            flash(
                "Login not successful. Please enter valid credentials",
                "danger")

    return render_template("login.html", title='Login', form=form)


@app.route("/logout")
def logout():
    """route that handles logout of users"""
    logout_user()
    return redirect(url_for("home"))

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = Listing.save_picture(form.picture.data)
            current_user.image_file = picture_file

        current_user.firstname = form.firstname.data
        current_user.lastname = form.lastname.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Account Updated', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.firstname.data = current_user.firstname
        form.lastname.data = current_user.lastname
        form.email.data = current_user.email
        image_file = url_for('static', filename='uploads/'
        + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)


@app.route("/listings/<listing_id>", methods=["GET"])
def listing(listing_id):
    """Listing resource"""
    if request.method == "GET":
        listing = LandListing.query.filter_by(id=listing_id).first()
        listing = listing if listing else HouseListing.query.filter_by(id=listing_id).first()
        if not listing:
            abort(404)

        return render_template("listing.html", title=listing.title,
                listing=listing)
