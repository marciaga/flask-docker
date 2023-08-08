from flask import Blueprint, jsonify, abort, make_response, request
from app.models.caretaker import Caretaker
from app.models.cat import Cat
from app import db
from .routes_helpers import validate_model

care_bp = Blueprint("caretakers", __name__, url_prefix="/caretakers")

# CREATE ENDPOINT
@care_bp.route("",methods=["POST"])
def create_caretaker():
  request_body = request.get_json()
  new_caretaker = Caretaker(name=request_body["name"])

  db.session.add(new_caretaker)
  db.session.commit()

  return make_response(f"caretaker {new_caretaker.name} successfully created", 201)

# GET ONE ENDPOINT

@care_bp.route("/<caretaker_id>", methods=["GET"])
def handle_one_caretaker(caretaker_id):
  caretaker = validate_model(caretaker_id)
  caretaker_dict = {"id": caretaker.id, "name": caretaker.name}
  
  return jsonify(caretaker_dict), 200

@care_bp.route("/<caretaker_id>/cats", methods=["POST"])
def create_cat(caretaker_id):
  caretaker = validate_model(caretaker_id)
  request_body = request.get_json()

  new_cat = Cat.from_dict(request_body,caretaker)

  db.session.add(new_cat)
  db.session.commit()

  return make_response(f"Cat {new_cat.name} successfully created with Caretaker {caretaker.name}", 201)

# GET ALL CATS BY CARETAKER ENDPOINT
@care_bp.route("/<caretaker_id>/cats", methods=["GET"])
def handle_cats_from_caretaker(caretaker_id):
  caretaker = validate_model(caretaker_id)

  cats_response = []
  for cat in caretaker.cats:
    cats_response.append(cat.to_dict())

  return jsonify(cats_response), 200