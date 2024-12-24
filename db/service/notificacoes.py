from db.init import get_db_connection


def db_get_notificacoes_by_professor(idProfessor: str):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        SELECT alunoId, nome, situacaoPagamento, situacaoTreino
        FROM alunos
        WHERE professorId = %s
          AND (situacaoPagamento = 'atrasado' OR situacaoTreino != 'regular');
    """
    cursor.execute(query, (idProfessor,))
    notificacoes = cursor.fetchall()
    cursor.close()
    connection.close()
    return notificacoes
