from flask import Blueprint, request, jsonify
from reserva_model import Reserva
from database import db
import requests
from reserva_model import create_reserva

routes = Blueprint("routes", __name__)

@routes.route("/reservas", methods=["POST"])
def criar_reserva():
    dados = request.json
    reserva = create_reserva(dados)
    return jsonify(reserva)

@routes.route("/reservas", methods=["GET"])
def listar_reservas():
    reservas = Reserva.query.all()
    return jsonify([
        {
            "id": r.id,
            "turma_id": r.turma_id,
            "sala": r.sala,
            "data": r.data,
            "hora_inicio": r.hora_inicio,
            "hora_fim": r.hora_fim
        } for r in reservas
    ])
