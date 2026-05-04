# INSTALANDO A APLICAÇÃO:
# python3 -m venv venv
# source venv/bin/activate
# pip install "fastapi[all]" sqlalchemy


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.responses import JSONResponse

app = FastAPI()

# Configurando CORS
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# Modelo Pydantic (validação automática)
class User(BaseModel):
    id: int
    name: str

# "Banco de dados" em memória
users: List[User] = [
    User(id=1, name="Maria"),
    User(id=2, name="João")
]

# Helper para forçar UTF-8 no retorno
def utf8_json_response(content, status_code=200):
    return JSONResponse(
        content=content,
        status_code=status_code,
        media_type="application/json; charset=utf-8"
    )

# GET - listar todos os usuários
@app.get("/users", response_model=List[User])
def get_users():
    return utf8_json_response([u.model_dump() for u in users])

# GET - buscar um usuário pelo id
@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    user = next((u for u in users if u.id == user_id), None)
    if user:
        return utf8_json_response(user.model_dump())
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

# POST - criar um novo usuário
@app.post("/users", response_model=User, status_code=201)
def create_user(user: User):
    users.append(user)
    return utf8_json_response(user.model_dump(), status_code=201)

# PUT - atualizar um usuário existente
@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, data: User):
    for i, u in enumerate(users):
        if u.id == user_id:
            users[i] = data
            return utf8_json_response(data.model_dump())
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

# DELETE - remover usuário
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    global users
    new_users = [u for u in users if u.id != user_id]
    if len(new_users) == len(users):
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    users = new_users
    return utf8_json_response({"msg": f"Usuário {user_id} removido"})


# Iniciando servidor
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "fastAPI:app",   # nome_do_arquivo:variavel_app
        host="127.0.0.1",
        port=3344,
        reload=True          # recarrega automaticamente ao editar
    )