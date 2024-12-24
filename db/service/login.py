from db.init import get_db_connection


def db_login_professor(email: str, senha: str):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        SELECT 
            professorId, 
            nome, 
            email, 
            senha,
            ativo
        FROM 
            professores
        WHERE 
            email = %s
            AND ativo = TRUE;
    """
    cursor.execute(query, (email,))
    professor = cursor.fetchone()
    print(professor)
    cursor.close()
    connection.close()
    if professor and professor[3] == senha and professor[4] == 1:
        professor = {
            "id": professor[0],
            "nome": professor[1],
            "email": professor[2],
            "role": "professor",
        }
        return professor
    else:
        return None
