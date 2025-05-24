import requests

TURMA_SERVICE_URL = "http://localhost:5000/turmas"

class ReservaService:
    @staticmethod
    def validar_turma(turma_id):
        url = f"{TURMA_SERVICE_URL}/{turma_id}"
        response = requests.get(url)
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if data["id"] == turma_id:
                return True
            else:
                print(f"ID da turma não corresponde. Esperado: {turma_id}, Recebido: {data.get('id')}")
                return False
        except requests.RequestException as e:
            print(f"Erro ao acessar o turma_service: {e}")
            return False