from db.init import get_db_connection


def db_create_new_treino(
    idProfessor: int, titulo: str, descricao: str, movimentos: list
):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        INSERT INTO treinos (professorId, titulo, descricao)
        VALUES (%s, %s, %s);
    """
    cursor.execute(query, (idProfessor, titulo, descricao))
    id_treino = cursor.lastrowid
    for movimento in movimentos:
        query = """
            INSERT INTO movimentos (professorId, titulo)
            VALUES (%s, %s);
        """
        cursor.execute(query, (idProfessor, movimento.titulo))
        id_movimento = cursor.lastrowid
        query = """
            INSERT INTO treino_movimento_relacionamentos (treinoId, movimentoId)
            VALUES (%s, %s);
        """
        cursor.execute(query, (id_treino, id_movimento))
        for descricao in movimento.descricoes:
            query = """
                INSERT INTO descricoes_movimentos (movimentoId, descricao)
                VALUES (%s, %s);
            """
            cursor.execute(query, (id_movimento, descricao.descricao))
    connection.commit()
    cursor.close()
    connection.close()
    return id_treino


def db_get_treinos_by_professor_id(id_professor: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        SELECT treinoId, titulo, descricao FROM treinos WHERE professorId = %s;
    """
    cursor.execute(query, (id_professor,))
    treinos = cursor.fetchall()
    cursor.close()
    connection.close()
    return treinos


def db_get_all_movimentos(idProfessor: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        SELECT movimentoId, titulo FROM movimentos WHERE professorId = %s;
    """
    cursor.execute(query, (idProfessor,))
    movimentos = cursor.fetchall()
    cursor.close()
    connection.close()
    return movimentos


def db_get_movimento_by_id(idMovimento: int, idProfessor: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)  # Retorna os resultados como dicionário
    query = """
        SELECT 
            m.movimentoId,
            m.titulo,
            d.descricaoMovimentoId,
            d.descricao
        FROM 
            movimentos m
        LEFT JOIN 
            descricoes_movimentos d ON m.movimentoId = d.movimentoId
        WHERE 
            m.movimentoId = %s AND m.professorId = %s;
    """
    cursor.execute(query, (idMovimento, idProfessor))
    resultados = cursor.fetchall()
    cursor.close()
    connection.close()

    if not resultados:
        return None

    return resultados
