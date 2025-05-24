from flask import request, jsonify
import requests
from database import db

class Reserva(db.Model):
    __tablename__ = 'reservas'

    id = db.Column(db.Integer, primary_key=True)
    turma_id = db.Column(db.Integer, nullable=False)
    sala = db.Column(db.String(50), nullable=False)
    data = db.Column(db.String(20), nullable=False)
    hora_inicio = db.Column(db.String(10), nullable=False)
    hora_fim = db.Column(db.String(10), nullable=False)

    def __init__(self, turma_id, sala, data, hora_inicio, hora_fim):
        self.turma_id = turma_id
        self.sala = sala
        self.data = data
        self.hora_inicio = hora_inicio
        self.hora_fim = hora_fim
    
    def to_dict(self):
        return {
            'id': self.id,
            'turma_id': self.turma_id,
            'sala': self.sala,
            'data': self.data,
            'hora_inicio': self.hora_inicio,
            'hora_fim': self.hora_fim
        }

def validar_turma(turma_id):
    resp = requests.get(f"http://localhost:5000/turmas/{turma_id}")
    print(resp)
    return resp.status_code == 200

def getReserva():
    reservas = Reserva.query.all()
    listar_reservas = []
    for reservas in reservas:
        listar_reservas.append(reservas.to_dict())
    return listar_reservas
    
def createReserva(dados):
    turma_id = dados.get("turma_id")

    if not validar_turma(turma_id):
        return jsonify({"erro": "Turma não encontrada"}), 400

    novaReserva = Reserva(
        turma_id=turma_id,
        sala=dados.get("sala"),
        data=dados.get("data"),
        hora_inicio=dados.get("hora_inicio"),
        hora_fim=dados.get("hora_fim")
    )

    db.session.add(novaReserva)
    db.session.commit()

    return novaReserva.to_dict()