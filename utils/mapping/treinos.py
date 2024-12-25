def map_movimentos_by_professor_response(dados):
    movimentos = []
    for movimentoId, titulo in dados:
        movimento = {
            "movimentoId": movimentoId,
            "titulo": titulo,
        }
        movimentos.append(movimento)
    return movimentos


def map_movimento_by_id_response(dados):
    movimento = {
        "movimentoId": dados[0]["movimentoId"],
        "titulo": dados[0]["titulo"],
        "descricoes": [],
    }
    for row in dados:
        if row["descricaoMovimentoId"]:
            movimento["descricoes"].append(
                {
                    "descricaoMovimentoId": row["descricaoMovimentoId"],
                    "descricao": row["descricao"],
                }
            )
    return movimento
