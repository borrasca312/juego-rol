"""
Flask routes for estado_personalizado
"""
from flask import Blueprint, jsonify, request
import services.estado_personalizado_service as service

bp = Blueprint("estado_personalizado", __name__, url_prefix="/estado_personalizados")

@bp.route("/", methods=["GET"])
def list_estado_personalizados():
    return jsonify(service.list_estado_personalizados())
