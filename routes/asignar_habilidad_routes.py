"""
Flask routes for asignar_habilidad
"""
from flask import Blueprint, jsonify, request
import services.asignar_habilidad_service as service

bp = Blueprint("asignar_habilidad", __name__, url_prefix="/asignar_habilidads")

@bp.route("/", methods=["GET"])
def list_asignar_habilidads():
    return jsonify(service.list_asignar_habilidads())
