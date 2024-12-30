from db.init import get_db_connection

from utils.init_db_query import create_table_query


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
            p.professorId AS professorId,
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


def db_vincular_planilha_aluno(
    idPlanilha: int, dataInicio: str, dataFim: str, alunos: list
):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
            INSERT INTO alunos_planilhas (alunoId, planilhaId, dataInicio, dataFim)
            VALUES (%s, %s, %s, %s);
        """
        for aluno in alunos:
            cursor.execute(query, (aluno, idPlanilha, dataInicio, dataFim))
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except:
        cursor.close()
        connection.close()
        return False


def db_get_planilhas_ativas_by_aluno(idAluno: int, dataBuscada: str):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = """
        SELECT
            p.planilhaId AS planilhaId,
            p.titulo AS tituloPlanilha,
            p.descricao AS descricaoPlanilha,
            p.professorId AS professorId,
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
            p.planilhaId IN (
                SELECT planilhaId
                FROM alunos_planilhas
                WHERE alunoId = %s AND dataInicio <= %s AND dataFim >= %s
            );
    """
    cursor.execute(query, (idAluno, dataBuscada, dataBuscada))
    planilha = cursor.fetchall()
    cursor.close()
    connection.close()
    return planilha


if __name__ == "__main__":
    print(db_get_planilhas_ativas_by_aluno(2, "2024-03-15"))
