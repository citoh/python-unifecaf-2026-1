# INSTALANDO A APLICAÇÃO:
# python3 -m venv venv
# source venv/bin/activate
# pip install flask flask-cors

from flask import Flask, Response, request
from flask_cors import CORS
import json

app = Flask(__name__)

# Garante que o JSON será ASCII (acentos, emojis etc.)
app.config["JSON_AS_ASCII"] = False

# Configurando CORS
CORS(app)

def json_response(payload, status=200):
    #Retorna JSON com Content-Type explícito em UTF-8
    return Response(
        json.dumps(payload, ensure_ascii=False),
        status=status,
        mimetype="application/json; charset=utf-8"
    )

# "Banco de dados" em memória
users = [
    {"id": 1, "name": "Maria"},
    {"id": 2, "name": "João"}
]

# GET - listar todos os usuários
@app.route("/users", methods=["GET"])
def get_users():
    return json_response(users)

# GET - buscar um usuário pelo id
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return json_response(user)
    return json_response({"error": "Usuário não encontrado"}, status=404)

# POST - criar um novo usuário
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json(silent=True) or {}
    users.append(data)
    return json_response(data, status=201)  # 201 Created

# PUT - atualizar um usuário existente
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json(silent=True) or {}
    for user in users:
        if user["id"] == user_id:
            user.update(data)
            return json_response(user)
    return json_response({"error": "Usuário não encontrado"}, status=404)

# DELETE - remover usuário
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    before = len(users)
    users = [u for u in users if u["id"] != user_id]
    if len(users) == before:
        return json_response({"error": "Usuário não encontrado"}, status=404)
    return json_response({"msg": f"Usuário {user_id} removido"})

if __name__ == "__main__":
    app.run(debug=True, port=3344)