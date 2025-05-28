# API de Reservas de Salas 🏫

API para gerenciamento de reservas de salas de aula, integrada ao serviço de Sistema Escolar.

## Descrição
- Gerencia reservas de salas com verificação de disponibilidade
- Valida turmas existentes através de integração com microsserviço de Sistema Escolar 
- Tecnologias: Python/Flask, SQLAlchemy, Docker

## Execução com Docker

### Pré-requisitos
- Docker instalado

### Passos
1. Construa a imagem:
   ```bash
   docker build -t api-reservas .
2. Execute o container:
   ```bash
   docker run -d -p 5001:5001 --name api-reservas api-reservas .
2. Abra o navegador usado:
   ```bash
   http://localhost:5001/reservas .
### Endpoints principais
   
- GET /reservas - Lista todas as reservas

- GET /reservas/<id> - Busca reserva por ID

- POST /reservas - Cria nova reserva

### Fluxo Principal
- Cliente faz requisição para API de Reservas

- API valida turma com serviço externo (5000)

- Verifica disponibilidade da sala

- Persiste reserva no banco SQLite

### Protocolos de Integração
- Comunicação síncrona via HTTP REST
- Formato JSON para todas as requisições

### Modelo de Dados
1. Python
   ```bash
   class Reserva(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       turma_id = db.Column(db.Integer, nullable=False)
       sala = db.Column(db.String(50), nullable=False)
       data = db.Column(db.String(20), nullable=False)
       hora_inicio = db.Column(db.String(10), nullable=False)
       hora_fim = db.Column(db.String(10), nullable=False) .

Desenvolvimento
Estrutura de Arquivos
api/
├── app.py               # Aplicação principal
├── controllers/         # Rotas
├── models/              # Modelos de dados
├── services/            # Lógica de negócio
└── database.py          # Configuração do banco
Variáveis de Ambiente
SQLALCHEMY_DATABASE_URI: Connection string do banco

TURMA_SERVICE_URL: URL do serviço de turmas

Exemplo de Requisição
bash
POST /reservas
{
    "turma_id": 1,
    "sala": "A101",
    "data": "2023-11-20",
    "hora_inicio": "14:00",
    "hora_fim": "16:00"
}
