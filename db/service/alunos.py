from db.init import get_db_connection


def db_get_alunos_by_professor(idProfessor: str):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        SELECT 
            a.alunoId AS alunoId,
            a.nome AS nomeAluno,
            g.grupoId AS grupoId,
            g.nome AS nomeGrupo,
            sg.subGrupoId AS subGrupoId,
            sg.nome AS nomeSubGrupo,
            a.situacaoPagamento AS statusPagamento
        FROM 
            alunos a
        LEFT JOIN 
            alunos_grupos ag ON a.alunoId = ag.alunoId
        LEFT JOIN 
            grupos g ON ag.grupoId = g.grupoId
        LEFT JOIN 
            alunos_sub_grupos asg ON a.alunoId = asg.alunoId
        LEFT JOIN 
            sub_grupos sg ON asg.subGrupoId = sg.subGrupoId
        WHERE 
            a.professorId = %s;
    """
    cursor.execute(query, (idProfessor,))
    alunos = cursor.fetchall()
    cursor.close()
    connection.close()
    return alunos


def db_get_alunos_by_professor_and_grupo(idProfessor: str, idGrupo: str):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        SELECT 
            a.alunoId,
            a.nome
        FROM 
            alunos a
        INNER JOIN 
            alunos_grupos ag ON a.alunoId = ag.alunoId
        INNER JOIN 
            grupos g ON ag.grupoId = g.grupoId
        INNER JOIN 
            professores p ON g.professorId = p.professorId
        WHERE 
            p.professorId = %s
            AND g.grupoId = %s; 
    """
    cursor.execute(query, (idProfessor, idGrupo))
    alunos = cursor.fetchall()
    cursor.close()
    connection.close()
    return alunos


def db_get_alunos_by_professor_grupo_and_subgrupo(
    idProfessor: str, idGrupo: str, idSubGrupo: str
):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        SELECT 
            a.alunoId,
            a.nome
        FROM 
            alunos a
        INNER JOIN 
            alunos_grupos ag ON a.alunoId = ag.alunoId
        INNER JOIN 
            grupos g ON ag.grupoId = g.grupoId
        INNER JOIN 
            alunos_sub_grupos asg ON a.alunoId = asg.alunoId
        INNER JOIN 
            sub_grupos sg ON asg.subGrupoId = sg.subGrupoId
        INNER JOIN 
            professores p ON g.professorId = p.professorId
        WHERE 
            p.professorId = %s
            AND g.grupoId = %s
            AND sg.subGrupoId = %s;
    """
    cursor.execute(query, (idProfessor, idGrupo, idSubGrupo))
    alunos = cursor.fetchall()
    cursor.close()
    connection.close()
    return alunos


def db_get_aluno_by_firebase_id(firebaseId: str):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        SELECT
            alunoId,
            firebaseId,
            nome,
            email,
            dataNascimento,
            dataCadastro,
            situacaoPagamento,
            situacaoTreino,
            ativo
        FROM
            alunos
        WHERE
            firebaseId = %s;
    """
    cursor.execute(query, (firebaseId,))
    aluno = cursor.fetchone()
    cursor.close()
    connection.close()
    return aluno


def db_create_new_aluno(firebaseId: str, nome: str, email: str, senha: str):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        INSERT INTO alunos (firebaseId, nome, email, senha)
        VALUES (%s, %s, %s, %s);
    """
    cursor.execute(query, (firebaseId, nome, email, senha))
    connection.commit()
    cursor.close()
    connection.close()
    return cursor.lastrowid


def db_get_aluno_by_email(email: str):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        SELECT
            alunoId,
            nome,
            email,
            dataCadastro
        FROM
            alunos
        WHERE
            email = %s;
    """
    cursor.execute(query, (email,))
    aluno = cursor.fetchone()
    cursor.close()
    connection.close()
    return aluno


def db_vincular_professor_a_aluno(idProfessor: str, idAluno: str):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
            UPDATE alunos
            SET professorId = %s
            WHERE alunoId = %s;
        """
        cursor.execute(query, (idProfessor, idAluno))
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except:
        cursor.close()
        connection.close()
        return False
