"""
Flask routes for raza
"""
from flask import Blueprint, jsonify, request
import services.raza_service as service

bp = Blueprint("raza", __name__, url_prefix="/razas")

@bp.route("/", methods=["GET"])
def list_razas():
    return jsonify(service.list_razas())
