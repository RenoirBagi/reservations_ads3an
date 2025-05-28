from flask import Blueprint, request, jsonify
import requests
from .reserva_model import Reserva, createReserva, getReserva, getReservaById, ReservaNaoEncontrada

routes = Blueprint("routes", __name__)

@routes.route('/reservas', methods=['GET'])
def get_reservas():
    reserva = getReserva()
    return jsonify(reserva)

@routes.route('/reservas/<int:id_reserva>', methods=['GET'])
def get_reservas_by_id(id_reserva):
    try:
        reserva = getReservaById(id_reserva)
        return jsonify(reserva)
    except ReservaNaoEncontrada:
        return jsonify({"erro": "Turma nao encontrada","código": 404})

@routes.route('/reservas', methods=['POST'])
def criar_reserva():
    dados = request.json
    reserva = createReserva(dados)
    return reserva
