"""
Flask routes for asignar_estado
"""
from flask import Blueprint, jsonify, request
import services.asignar_estado_service as service

bp = Blueprint("asignar_estado", __name__, url_prefix="/asignar_estados")

@bp.route("/", methods=["GET"])
def list_asignar_estados():
    return jsonify(service.list_asignar_estados())
