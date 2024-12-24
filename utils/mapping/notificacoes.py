def map_notificacoes_by_professor_response(dados):
    notificacoes = []

    for id, nome, situacaoPagamento, situacaoTreino in dados:
        aluno_com_notificacao = {
            "id": id,
            "nome": nome,
            "situacaoPagamento": situacaoPagamento,
            "situacaoTreino": situacaoTreino,
        }

        notificacoes.append(aluno_com_notificacao)

    return notificacoes
