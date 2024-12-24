import json
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from db.init import init_db

from db.service.login import db_login_professor

from db.service.grupos import db_get_grupos_by_professor
from utils.mapping.grupos import map_grupos_by_professor_response

from db.service.notificacoes import db_get_notificacoes_by_professor
from utils.mapping.notificacoes import map_notificacoes_by_professor_response

from db.service.alunos import (
    db_get_alunos_by_professor,
    db_get_alunos_by_professor_and_grupo,
    db_get_alunos_by_professor_grupo_and_subgrupo,
)
from utils.mapping.alunos import map_alunos_in_id_nome, map_alunos

from schemas.Login import BodyRequestLogin

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
    else:
        return JSONResponse(
            status_code=401,
            content={"message": "Credenciais inválidas"},
        )


@app.get("/api/v1/grupos/{idProfessor}")
def get_grupos_by_professor(idProfessor: str):
    grupos = db_get_grupos_by_professor(idProfessor)
    grupos_mapeados = map_grupos_by_professor_response(grupos)
    return grupos_mapeados


@app.get("/api/v1/notificacoes/{idProfessor}")
def get_notificacoes_by_professor(idProfessor: str):
    notificacoes = db_get_notificacoes_by_professor(idProfessor)
    notificacoes_mapeadas = map_notificacoes_by_professor_response(notificacoes)
    return notificacoes_mapeadas


@app.get("/api/v1/alunos/{idProfessor}")
def get_alunos_by_professor(idProfessor: str):
    alunos = db_get_alunos_by_professor(idProfessor)
    alunos_mapeados = map_alunos(alunos)
    return alunos_mapeados


@app.get("/api/v1/alunos/{idProfessor}/grupo/{idGrupo}")
def get_alunos_by_professor_and_grupo(idProfessor: str, idGrupo: str):
    alunos = db_get_alunos_by_professor_and_grupo(idProfessor, idGrupo)
    alunos_mapeados = map_alunos_in_id_nome(alunos)
    return alunos_mapeados


@app.get("/api/v1/alunos/{idProfessor}/grupo/{idGrupo}/subgrupo/{idSubGrupo}")
def get_alunos_by_professor_grupo_and_subgrupo(
    idProfessor: str, idGrupo: str, idSubGrupo: str
):
    alunos = db_get_alunos_by_professor_grupo_and_subgrupo(
        idProfessor, idGrupo, idSubGrupo
    )
    alunos_mapeados = map_alunos_in_id_nome(alunos)
    return alunos_mapeados
