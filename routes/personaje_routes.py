"""
Flask routes for personaje
"""
from flask import Blueprint, jsonify, request
import services.personaje_service as service

bp = Blueprint("personaje", __name__, url_prefix="/personajes")

@bp.route("/", methods=["GET"])
def list_personajes():
    return jsonify(service.list_personajes())
