"""
Flask routes for partida
"""
from flask import Blueprint, jsonify, request
import services.partida_service as service

bp = Blueprint("partida", __name__, url_prefix="/partidas")

@bp.route("/", methods=["GET"])
def list_partidas():
    return jsonify(service.list_partidas())
