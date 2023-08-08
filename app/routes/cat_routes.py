from flask import Blueprint, jsonify, abort, make_response, request
from app.models.cat import Cat
from app import db
from .routes_helpers import validate_model

bp = Blueprint("cats", __name__, url_prefix="/cats")


# GET ALL ENDPOINT
@bp.route("", methods=["GET"])
def handle_cats():

    personality_param = request.args.get("personality")
    color_param = request.args.get("color")

    cat_query = Cat.query

    if personality_param:
        cat_query = cat_query.filter(
            Cat.personality.ilike(f"%{personality_param}%"))

    if color_param:
        cat_query = cat_query.filter_by(color=color_param)

    cats = cat_query.order_by(Cat.id).all()
    cats_list = [cat.to_dict() for cat in cats]

    return jsonify(cats_list), 200


# CREATE ENDPOINT
@bp.route("", methods=["POST"])
def create_cat():
    request_body = request.get_json()

    new_cat = Cat.from_dict(request_body)

    db.session.add(new_cat)
    db.session.commit()

    return jsonify(new_cat.to_dict()), 201


# GET ONE ENDPOINT
@bp.route("/<id>", methods=["GET"])
def handle_cat(id):
    cat = validate_model(Cat, id)

    return jsonify(cat.to_dict()), 200


# UPDATE ONE ENDPOINT
@bp.route("/<id>", methods=["PUT"])
def update_cat(id):
    cat = validate_model(Cat, id)
    request_body = request.get_json()

    cat.color = request_body["color"]
    cat.personality = request_body["personality"]
    cat.name = request_body["name"]

    db.session.commit()

    return make_response(f"Cat {cat.name} successfully updated", 200)

# UPDATE PET COUNT ENDPOINT
@bp.route("/<id>/pet", methods=["PATCH"])
def pet_cat_with_id(id):
    cat = validate_model(Cat, id)
    cat.pet_count += 1

    db.session.commit()
    return jsonify(cat.to_dict()), 200


# DELETE ONE ENDPOINT
@bp.route("/<id>", methods=["DELETE"])
def delete_cat(id):
    cat = validate_model(Cat, id)

    db.session.delete(cat)
    db.session.commit()

    return make_response(f"Cat {cat.name} successfully deleted", 200)



