from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from datetime import datetime

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
    db_get_aluno_by_firebase_id,
    db_create_new_aluno,
    db_get_aluno_by_email,
    db_vincular_professor_a_aluno,
)
from utils.mapping.alunos import (
    map_alunos_in_id_nome,
    map_alunos,
    map_aluno_by_firebase_id_response,
    map_aluno_by_email_response,
)

from db.service.treinos import (
    db_create_new_treino,
    db_get_all_movimentos,
    db_get_movimento_by_id,
    db_get_treinos_by_professor_id,
)
from utils.mapping.treinos import (
    map_movimentos_by_professor_response,
    map_movimento_by_id_response,
    map_treinos_by_professor_response,
)

from db.service.planilhas import (
    db_get_all_modelos,
    db_get_planilha_by_id,
    db_create_new_planilha,
    db_vincular_planilha_aluno,
    db_get_planilha_ativa_by_aluno,
    db_get_bloco_by_id,
    db_get_historico_planilhas_by_aluno,
)
from utils.mapping.planilhas import (
    map_modelos_by_professor_response,
    map_planilha_ativa_by_aluno_response,
    map_planilha_by_id_response,
    map_bloco_by_id_response,
    map_historico_planilhas_by_aluno_response,
)


from schemas.Login import BodyRequestLogin
from schemas.Grupo import BodyRequestInsertGrupo, BodyRequestInsertSubGrupo
from schemas.Treino import BodyRequestCreateTreino
from schemas.Planilha import BodyRequestCreatePlanilha, BodyRequestVincular
from schemas.Aluno import BodyRequestCreateAluno, BodyRequestVincularProfessorAluno

from utils.verifica_owner_planilha import verifica_owner_planilha

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "exp://192.168.1.172:8081",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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


@app.get("/api/v1/treinos/{idProfessor}")
def get_treinos_by_professor(idProfessor: str):
    treinos = db_get_treinos_by_professor_id(idProfessor)
    mapped_treinos = map_treinos_by_professor_response(treinos)
    return mapped_treinos


@app.get("/api/v1/movimentos/{idProfessor}")
def get_movimentos_by_professor(idProfessor: str):
    movimentos = db_get_all_movimentos(idProfessor)
    mapped_movimentos = map_movimentos_by_professor_response(movimentos)
    return mapped_movimentos


@app.get("/api/v1/movimento/{idMovimento}/{idProfessor}")
def get_movimento_by_id(idMovimento: str, idProfessor: str):
    movimento = db_get_movimento_by_id(idMovimento, idProfessor)
    mapped_movimento = map_movimento_by_id_response(movimento)
    return mapped_movimento


@app.get("/api/v1/planilha/modelos/{idProfessor}")
def get_modelos_planilha_by_professor(idProfessor: str):
    modelos = db_get_all_modelos(idProfessor)
    mapped_modelos = map_modelos_by_professor_response(modelos)
    return mapped_modelos


@app.get("/api/v1/planilha/{idPlanilha}")
def get_planilha_by_id(idPlanilha: str):
    planilha = db_get_planilha_by_id(idPlanilha)
    mapped_planilha = map_planilha_by_id_response(planilha)
    return mapped_planilha


@app.post("/api/v1/planilha/nova")
def create_new_planilha(request: BodyRequestCreatePlanilha):
    id_planilha = db_create_new_planilha(
        request.idProfessor, request.titulo, request.descricao, request.sessoes
    )
    if id_planilha:
        return {"message": "Planilha inserida com sucesso", "id": id_planilha}
    return JSONResponse(
        status_code=500,
        content={"message": "Erro ao inserir planilha"},
    )


@app.post("/api/v1/planilha/{idPlanilha}/vincular")
def vincular_planilha_a_aluno(request: BodyRequestVincular, idPlanilha: str):
    verificador = verifica_owner_planilha(request.idProfessor, idPlanilha)
    if not verificador:
        return JSONResponse(
            status_code=401,
            content={"message": "Você não tem permissão para vincular essa planilha"},
        )
    resultado = db_vincular_planilha_aluno(
        idPlanilha, request.dataInicio, request.dataFim, request.alunos
    )
    if resultado:
        return {"message": "Planilha vinculada com sucesso"}
    return JSONResponse(
        status_code=500,
        content={"message": "Erro ao vincular planilha"},
    )


@app.get("/api/v1/aluno/{firebaseId}")
def get_aluno_by_firebase_id(firebaseId: str):
    aluno = db_get_aluno_by_firebase_id(firebaseId)
    mapped_aluno = map_aluno_by_firebase_id_response(aluno)
    return mapped_aluno


@app.post("/api/v1/aluno/novo")
def create_new_aluno(request: BodyRequestCreateAluno):
    id_aluno = db_create_new_aluno(
        request.firebaseId, request.nome, request.email, request.senha
    )
    if id_aluno:
        return {"message": "Aluno inserido com sucesso", "id": id_aluno}
    return JSONResponse(
        status_code=500,
        content={"message": "Erro ao inserir aluno"},
    )


@app.get("/api/v1/aluno/email/{emailAluno}")
def get_aluno_by_email(emailAluno: str):
    aluno = db_get_aluno_by_email(emailAluno)
    mapped_aluno = map_aluno_by_email_response(aluno)
    return mapped_aluno


@app.post("/api/v1/vincular/professor/aluno")
def vincular_professor_a_aluno(request: BodyRequestVincularProfessorAluno):
    resultado = db_vincular_professor_a_aluno(request.idProfessor, request.idAluno)
    if resultado:
        return {"message": "Professor vinculado com sucesso"}
    return JSONResponse(
        status_code=500,
        content={"message": "Erro ao vincular professor"},
    )


@app.get("/api/v1/aluno/{idAluno}/planilha")
def get_planilha_ativa_by_aluno(idAluno: str):
    dataBuscada = datetime.now().strftime("%Y-%m-%d")
    planilha = db_get_planilha_ativa_by_aluno(idAluno, dataBuscada)
    mapped_planilha = map_planilha_ativa_by_aluno_response(planilha)
    return mapped_planilha


@app.get("/api/v1/bloco/{idBloco}")
def get_bloco_by_id(idBloco: str):
    bloco = db_get_bloco_by_id(idBloco)
    mapped_bloco = map_bloco_by_id_response(bloco, idBloco)
    return mapped_bloco


@app.get("/api/v1/aluno/{idAluno}/planilha/historico")
def get_historico_planilhas_by_aluno(idAluno: str):
    dataBuscada = datetime.now().strftime("%Y-%m-%d")
    historico_planilhas = db_get_historico_planilhas_by_aluno(idAluno, dataBuscada)
    mapped_historico_planilhas = map_historico_planilhas_by_aluno_response(
        historico_planilhas
    )
    return mapped_historico_planilhas
