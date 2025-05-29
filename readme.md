# API de Reservas de Salas 🏫

API para gerenciamento de reservas de salas de aula, integrada ao serviço de Sistema Escolar.

## Descrição
A API Reservas é um microsserviço responsável pela manipulação de reservas de salas, permitindo a criação e a consulta de uma ou mais reservas existentes. Este serviço opera de forma integrada com a API Sistema Escolar, da qual depende para validações essenciais.

## Funcionalidades principais:
###### Criação de reserva: Ao receber uma solicitação de reserva, a API realiza:

   - Validação da existência da turma solicitante, por meio de uma consulta à API Sistema Escolar.
   - Verificação da disponibilidade da sala desejada.

###### Consulta de reservas: É possível buscar:

   - Uma reserva específica, a partir de seu Id.
   - Todas as reservas registradas.

## Tecnologias utilizadas:
- Python com Flask (framework web)

- SQLAlchemy (ORM para acesso ao banco de dados)

- Docker (containerização do serviço)

## Execução com Docker

### Pré-requisitos
- Docker instalado

### Passos
1. Construa a imagem:
   ```bash
   docker build -t api-reservas .
2. Execute o container:
   ```bash
   docker run -d -p 5001:5001 --name api-reservas api-reservas
2. Abra o navegador e cole essa url:
   ```bash
   http://localhost:5001/reservas
## Endpoints principais
   
- GET /reservas - Lista todas as reservas

- GET /reservas/< id > - Busca reserva por ID

- POST /reservas - Cria nova reserva

## Ecossistema de Microserviços para Sistema Escolar
#### Validação de turma (turma_id):
   - Durante o processo de criação de uma reserva, o arquivo reserva_service.py realiza uma requisição à API Sistema Escolar, enviando o turma_id fornecido na solicitação.
   - Essa API, por sua vez, consulta a tabela turmas no banco de dados app.db em busca de uma turma com o id correspondente.
   - Caso a turma seja encontrada (isto é, o id retornado seja igual ao turma_id enviado), a validação da turma é considerada bem-sucedida, concluindo a primeira etapa do processo de criação da reserva.

## Protocolos de Integração
- Comunicação síncrona via HTTP REST
- Formato JSON para todas as requisições

## Modelo de Dados
- Python
   ```bash
   class Reserva(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       turma_id = db.Column(db.Integer, nullable=False)
       sala = db.Column(db.String(50), nullable=False)
       data = db.Column(db.String(20), nullable=False)
       hora_inicio = db.Column(db.String(10), nullable=False)
       hora_fim = db.Column(db.String(10), nullable=False) .

## Arquitetura
### MVC
  O projeto segue o padrão de arquitetura MVC (Model-View-Controller), promovendo separação de responsabilidades e facilitando a manutenção e escalabilidade do sistema.
   - Model (Modelo)
      - Local: api/models/reserva_model.py
      - Função: Define a estrutura da entidade Reserva com SQLAlchemy. Responsável por representar os dados e regras de persistência da aplicação.

   - Controller
      - Local: api/controllers/reserva_route.py
      - Função: Define as rotas (endpoints) da API, recebendo as requisições e encaminhando-as para os serviços apropriados. Atua como a camada que interage diretamente com o cliente da API (ex: front-end, outro sistema, etc).
        
### Estrutura de Arquivos
   - reservations_ADS3AN/
      ```bash
         ├──api/
            ├── controllers/         
            │   └── reserva_route.py   # Rotas
            ├── models/              
            │   └── reserva_model.py   # Modelos de dados
            ├── services/            
            │   └── reserva_service.py # Conexão com API Sistema Escolar
            ├── app.py                 # Aplicação principal
            ├── database.py            # Configuração do banco
            ├── test.py                # Teste da API
            ├── services/
            │   └── reservas.db        # Banco de Dados
            ├── dockerfile             # Criar imagem Docker
            ├── readme.md              # Documentação
            └── requirements.txt       # Dependências

## Exemplo de Requisição
   ```bash
      POST /reservas
      {
          "turma_id": 1,
          "sala": "A101",
          "data": "2023-11-20",
          "hora_inicio": "14:00",
          "hora_fim": "16:00"
      }
