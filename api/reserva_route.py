from flask import Blueprint, request, jsonify
from reserva_model import Reserva
from database import db
import requests
from reserva_model import createReserva, getReserva

routes = Blueprint("routes", __name__)

@routes.route("/reservas", methods=["GET"])
def get_reservas():
    reserva = getReserva()
    return jsonify(reserva)

@routes.route("/reservas", methods=["POST"])
def criar_reserva():
    dados = request.json
    reserva = createReserva(dados)
    return jsonify(reserva)
