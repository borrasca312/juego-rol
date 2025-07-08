"""
Flask routes for habilidad
"""
from flask import Blueprint, jsonify, request
import services.habilidad_service as service

bp = Blueprint("habilidad", __name__, url_prefix="/habilidads")

@bp.route("/", methods=["GET"])
def list_habilidads():
    return jsonify(service.list_habilidads())
