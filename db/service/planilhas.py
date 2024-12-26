# from db.init import get_db_connection

import os
import mysql.connector
from dotenv import load_dotenv

# from utils.init_db_query import create_table_query

load_dotenv()

db_config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
}


def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection


def db_get_all_modelos(idProfessor: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        SELECT modeloPlanilhaId, titulo, planilhaId FROM modelos_planilha WHERE professorId = %s;
    """
    cursor.execute(query, (idProfessor,))
    modelos = cursor.fetchall()
    cursor.close()
    connection.close()
    return modelos


def db_get_planilha_by_id(idPlanilha: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT 
            p.planilhaId AS planilhaId,
            p.titulo AS tituloPlanilha,
            p.descricao AS descricaoPlanilha,
            s.sessaoId AS idSessao,
            s.titulo AS tituloSessao,
            bt.blocoTreinoId AS idBlocoTreino,
            bt.titulo AS tituloBlocoTreino,
            t.treinoId AS idTreino,
            t.titulo AS tituloTreino
        FROM 
            planilhas p
        LEFT JOIN 
            sessoes s ON p.planilhaId = s.planilhaId
        LEFT JOIN 
            blocos_treino bt ON s.sessaoId = bt.sessaoId
        LEFT JOIN 
            treinos t ON bt.treinoId = t.treinoId
        WHERE 
            p.planilhaId = %s;
    """

    cursor.execute(query, (idPlanilha,))
    planilha = cursor.fetchall()
    cursor.close()
    connection.close()
    return planilha


def db_create_new_planilha(
    idProfessor: int, titulo: str, descricao: str, sessoes: list
):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        INSERT INTO planilhas (professorId, titulo, descricao)
        VALUES (%s, %s, %s);
    """
    cursor.execute(query, (idProfessor, titulo, descricao))
    id_planilha = cursor.lastrowid
    for sessao in sessoes:
        query = """
            INSERT INTO sessoes (planilhaId, titulo)
            VALUES (%s, %s);
        """
        cursor.execute(query, (id_planilha, sessao.titulo))
        id_sessao = cursor.lastrowid
        for bloco in sessao.blocos:
            query = """
                INSERT INTO blocos_treino (sessaoId, titulo, treinoId)
                VALUES (%s, %s, %s);
            """
            cursor.execute(query, (id_sessao, bloco.titulo, bloco.idTreino))
    connection.commit()
    cursor.close()
    connection.close()
    return id_planilha


if __name__ == "__main__":
    planilha = db_get_planilha_by_id(1)

    planilha_data = {
        "id": planilha[0]["planilhaId"],
        "titulo": planilha[0]["tituloPlanilha"],
        "descricao": planilha[0]["descricaoPlanilha"],
        "sessoes": [],
    }

    # Usando um dicionário para evitar duplicatas
    sessoes_dict = {}

    for sessao in planilha:
        sessao_id = sessao["idSessao"]

        if sessao_id not in sessoes_dict:
            # Se a sessão ainda não foi adicionada, cria um novo registro
            sessoes_dict[sessao_id] = {
                "id": sessao["idSessao"],
                "titulo": sessao["tituloSessao"],
                "blocos": [],
            }

        # Adiciona o bloco à sessão correspondente
        bloco = {
            "id": sessao["idBlocoTreino"],
            "titulo": sessao["tituloBlocoTreino"],
            "treino": {
                "id": sessao["idTreino"],
                "titulo": sessao["tituloTreino"],
            },
        }
        sessoes_dict[sessao_id]["blocos"].append(bloco)

    # Converte o dicionário de sessões em uma lista
    planilha_data["sessoes"] = list(sessoes_dict.values())

    # Exibindo a saída final
    print(planilha_data)
