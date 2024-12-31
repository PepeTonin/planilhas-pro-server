def map_alunos(dados):
    alunos = []
    for (
        aluno_id,
        aluno_nome,
        grupo_id,
        grupo_nome,
        subgrupo_id,
        subgrupo_nome,
        status_pagamento,
    ) in dados:
        aluno = {
            "id": aluno_id,
            "nome": aluno_nome,
            "grupoId": grupo_id,
            "grupoNome": grupo_nome,
            "subGrupoNome": subgrupo_nome,
            "subGrupoId": subgrupo_id,
            "statusPagamento": status_pagamento,
        }
        alunos.append(aluno)
    return alunos


def map_alunos_in_id_nome(dados):
    alunos = []
    for aluno_id, aluno_nome in dados:
        aluno = {"id": aluno_id, "nome": aluno_nome}
        alunos.append(aluno)
    return alunos


def map_aluno_by_firebase_id_response(dados):
    aluno = {
        "alunoId": dados[0],
        "firebaseId": dados[1],
        "nome": dados[2],
        "email": dados[3],
        "dataNascimento": dados[4],
        "dataCadastro": dados[5],
        "situacaoPagamento": dados[6],
        "situacaoTreino": dados[7],
        "ativo": dados[8],
        "role": "aluno",
    }
    return aluno
