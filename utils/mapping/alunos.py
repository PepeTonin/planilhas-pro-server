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
