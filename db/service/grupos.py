from db.init import get_db_connection


def db_get_grupos_by_professor(idProfessor: str):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        SELECT 
            g.grupoId AS id,
            g.nome,
            JSON_ARRAYAGG(
                JSON_OBJECT(
                    'id', sg.subGrupoId,
                    'nome', sg.nome
                )
            ) AS subgrupos
        FROM 
            grupos g
        LEFT JOIN 
            sub_grupos sg ON sg.grupoId = g.grupoId
        WHERE 
            g.professorId = %s
        GROUP BY 
            g.grupoId;
    """
    cursor.execute(query, (idProfessor,))
    grupos = cursor.fetchall()
    cursor.close()
    connection.close()
    return grupos


def db_insert_new_grupo(nome: str, idProfessor: str):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        INSERT INTO grupos (nome, professorId) VALUES (%s, %s);
    """
    cursor.execute(query, (nome, idProfessor))
    connection.commit()
    id_new_grupo = cursor.lastrowid
    cursor.close()
    connection.close()
    return id_new_grupo


def db_insert_new_subgrupo(nome: str, idGrupo: str):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        INSERT INTO sub_grupos (nome, grupoId) VALUES (%s, %s);
    """
    cursor.execute(query, (nome, idGrupo))
    connection.commit()
    id_new_subgrupo = cursor.lastrowid
    cursor.close()
    connection.close()
    return id_new_subgrupo
