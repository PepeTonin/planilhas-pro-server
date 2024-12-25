from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from db.init import init_db

from db.service.login import db_login_professor

from db.service.grupos import (
    db_get_grupos_by_professor,
    db_insert_new_grupo,
    db_insert_new_subgrupo,
)
from utils.mapping.grupos import map_grupos_by_professor_response

from db.service.notificacoes import db_get_notificacoes_by_professor
from utils.mapping.notificacoes import map_notificacoes_by_professor_response


from db.service.alunos import (
    db_get_alunos_by_professor,
    db_get_alunos_by_professor_and_grupo,
    db_get_alunos_by_professor_grupo_and_subgrupo,
)
from utils.mapping.alunos import map_alunos_in_id_nome, map_alunos

from db.service.treinos import db_create_new_treino

from schemas.Login import BodyRequestLogin
from schemas.Grupo import BodyRequestInsertGrupo, BodyRequestInsertSubGrupo
from schemas.Treino import BodyRequestCreateTreino

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.on_event("startup")
# def on_startup():
#     init_db()


@app.post("/api/v1/login/professor")
def login_professor(request: BodyRequestLogin):
    professor = db_login_professor(request.email, request.senha)
    if professor:
        return professor
    return JSONResponse(
        status_code=401,
        content={"message": "Credenciais inválidas"},
    )


@app.post("/api/v1/novo/grupo")
def insert_grupo(request: BodyRequestInsertGrupo):
    id_new_grupo = db_insert_new_grupo(request.nome, request.idProfessor)
    if id_new_grupo:
        return {"message": "Grupo inserido com sucesso", "id": id_new_grupo}
    return JSONResponse(
        status_code=500,
        content={"message": "Erro ao inserir grupo"},
    )


@app.post("/api/v1/novo/subgrupo")
def insert_grupo(request: BodyRequestInsertSubGrupo):
    id_new_subgrupo = db_insert_new_subgrupo(request.nome, request.idGrupo)
    if id_new_subgrupo:
        return {"message": "Subgrupo inserido com sucesso", "id": id_new_subgrupo}
    return JSONResponse(
        status_code=500,
        content={"message": "Erro ao inserir subgrupo"},
    )


@app.get("/api/v1/grupos/{idProfessor}")
def get_grupos_by_professor(idProfessor: str):
    grupos = db_get_grupos_by_professor(idProfessor)
    mapped_grupos = map_grupos_by_professor_response(grupos)
    return mapped_grupos


@app.get("/api/v1/notificacoes/{idProfessor}")
def get_notificacoes_by_professor(idProfessor: str):
    notificacoes = db_get_notificacoes_by_professor(idProfessor)
    mapped_notificacoes = map_notificacoes_by_professor_response(notificacoes)
    return mapped_notificacoes


@app.get("/api/v1/alunos/{idProfessor}")
def get_alunos_by_professor(idProfessor: str):
    alunos = db_get_alunos_by_professor(idProfessor)
    mapped_alunos = map_alunos(alunos)
    return mapped_alunos


@app.get("/api/v1/alunos/{idProfessor}/grupo/{idGrupo}")
def get_alunos_by_professor_and_grupo(idProfessor: str, idGrupo: str):
    alunos = db_get_alunos_by_professor_and_grupo(idProfessor, idGrupo)
    mapped_alunos = map_alunos_in_id_nome(alunos)
    return mapped_alunos


@app.get("/api/v1/alunos/{idProfessor}/grupo/{idGrupo}/subgrupo/{idSubGrupo}")
def get_alunos_by_professor_grupo_and_subgrupo(
    idProfessor: str, idGrupo: str, idSubGrupo: str
):
    alunos = db_get_alunos_by_professor_grupo_and_subgrupo(
        idProfessor, idGrupo, idSubGrupo
    )
    mapped_alunos = map_alunos_in_id_nome(alunos)
    return mapped_alunos


@app.post("/api/v1/treino/novo")
def create_new_treino(request: BodyRequestCreateTreino):
    id_treino = db_create_new_treino(
        request.idProfessor, request.titulo, request.descricao, request.movimentos
    )
    if id_treino:
        return {"message": "Treino inserido com sucesso", "id": id_treino}
    return JSONResponse(
        status_code=500,
        content={"message": "Erro ao inserir treino"},
    )
