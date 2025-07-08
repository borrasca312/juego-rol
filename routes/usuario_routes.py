"""
Flask routes for usuario
"""
from flask import Blueprint, jsonify, request
import services.usuario_service as service

bp = Blueprint("usuario", __name__, url_prefix="/usuarios")

@bp.route("/", methods=["GET"])
def list_usuarios():
    return jsonify(service.list_usuarios())
