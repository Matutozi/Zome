from flask import request, jsonify, Blueprint, abort
from zome import db
from zome.models import User, LandListing, HouseListing

api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/listings", methods=["GET"])
def listings():
    """listings resource"""
    if request.method == "GET":
        listings = [listing.to_dict() for listing in LandListing.query.all()]
        listings += [listing.to_dict() for listing in HouseListing.query.all()]
        return jsonify(listings), 200


@api.route("/listings/<listing_id>", methods=["GET"])
def listing(listing_id):
    """Listing resource"""
    if request.method == "GET":
        listing = LandListing.query.filter_by(id=listing_id).first()
        if not listing:
            listing = HouseListing.query.filter_by(id=listing_id).first()
        if not listing:
            abort(404)
        return jsonify(listing.to_dict()), 200


@api.route("/user/<user_id>", methods=["GET"])
def users(user_id):
    """Users resource"""
    if request.method == "GET":
        user = User.query.filter_by(id=user_id).first()
        if not user:
            abort(404)
        return jsonify(user.to_dict()), 200


@api.route("/homes", methods=["GET"])
def homes():
    """Homes resource"""
    if request.method == "GET":
        homes = HouseListing.query.all()
        return jsonify(homes), 200


@api.route("/lands", methods=["GET"])
def lands():
    """Lands resource"""
    if request.method == "GET":
        places = LandListing.query.all()
        return jsonify(places), 200


@api.route("/user/<user_id>/listings", methods=["GET", "POST"])
def user_listings(user_id):
    """User Listings Resource"""
    user = User.query.filter_by(id=user_id).first()
    if not user:
        abort(404)
    if request.method == "GET":
        listings = user.home_lisitings + user.land_listings
        listings = [listing.to_dict() for listing in listings]
        return jsonify(listings)
    if request.method == "POST":
        data = request.json
        if "type_of_listing" not in data:
            abort(404)
        if "type_of_listing" == "House":
            listing = HouseListing(**data)
        else:
            listing = LandListing(**data)
        db.session.add(listing)
        db.session.commit()
        return jsonify(listing.to_dict()), 201


@api.route(
        "/user/<user_id>/listing/<listing_id>",
        methods=["GET", "DELETE", "PUT"])
def user_listing(user_id, listing_id):
    "User Listing Resource"
    user = User.query.filter_by(id=user_id).first()
    if not user:
        abort(404)
    listing = LandListing.query.filter_by(id=listing_id).first()
    if not listing:
        listing = HouseListing.query.filter_by(id=listing_id).first()
    if not listing:
        abort(404)

    if request.method == "GET":
        return jsonify(listing.to_dict())
    if request.method == "DELETE":
        db.session.delete(listing)
        return jsonify({}), 200
    if request.method == "PUT":
        data = request.json
        for key, value in data:
            setattr(listing, key, value)
        db.session.add(listing)
        db.session.commit()
        return jsonify(listing.to_dict()), 200
