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
