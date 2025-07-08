"""
Flask routes for equipamiento
"""
from flask import Blueprint, jsonify, request
import services.equipamiento_service as service

bp = Blueprint("equipamiento", __name__, url_prefix="/equipamientos")

@bp.route("/", methods=["GET"])
def list_equipamientos():
    return jsonify(service.list_equipamientos())
