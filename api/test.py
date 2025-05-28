from flask import Flask, jsonify, request
import unittest
import requests

class TestStringMethods(unittest.TestCase):

     def test_000_reserva_retorna_lista(self):
          r = requests.get('http://localhost:5001/reservas')
          if r.status_code == 404:
               self.fail("Página /Reserva não definida no servidor para o método GET.")
          try:
               lista_reserva = r.json()
          except:
               self.fail("Formato deveria ser JSON.")
          self.assertEqual(type(lista_reserva), type([]))

     def test_001_reserva_retorna_por_id(self):
          r = requests.post('http://localhost:5001/reservas', json={"turma_id": 1, "sala": "Sala 106", "data": "2024-06-15", "hora_inicio": "01:00", "hora_fim": "01:30"})

          get = requests.get('http://localhost:5001/reservas')
          lista_turmas = get.json()
          last_index = lista_turmas[-1]['id']

          req_reserva = requests.get(f'http://localhost:5001/reservas/{last_index}')
          retorno = req_reserva.json()
          if req_reserva.status_code == 404:
                    self.fail("Página /reserva/id não definida no servidor para o método GET.")
                    
          self.assertEqual(type(retorno),type({}))

     def test_001_reserva_criacao(self):
          r = requests.post('http://localhost:5001/reservas', json={"turma_id": 2, "sala": "Sala 107", "data": "2024-06-15", "hora_inicio": "10:45", "hora_fim": "11:30"})
          print(r)
          if r.status_code == 404:
               self.fail("Página /reserva não definida no servidor para o método POST.")


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


if __name__ == '__main__':
    runTests()