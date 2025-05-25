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

     def test_001_reserva_criacao(self):
          r = requests.post('http://localhost:5001/reservas', json={"turma_id": 2, "sala": "Sala 102", "data": "2024-06-15", "hora_inicio": "08:00", "hora_fim": "08:30"})
          print(r)
          if r.status_code == 404:
               self.fail("Página /reserva não definida no servidor para o método POST.")


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


if __name__ == '__main__':
    runTests()