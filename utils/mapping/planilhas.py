def map_modelos_by_professor_response(dados):
    modelos = []
    for modeloPlanilhaId, titulo, planilhaId in dados:
        modelo = {
            "id": modeloPlanilhaId,
            "title": titulo,
            "workoutPlanId": planilhaId,
        }
        modelos.append(modelo)
    return modelos


def map_planilha_by_id_response(dados):

    planilha = {
        "id": dados[0]["planilhaId"],
        "title": dados[0]["tituloPlanilha"],
        "description": dados[0]["descricaoPlanilha"],
        "owner": dados[0]["professorId"],
        "sessions": [],
    }

    sessoes_dict = {}

    for sessao in dados:
        sessao_id = sessao["idSessao"]
        if sessao_id not in sessoes_dict:
            sessoes_dict[sessao_id] = {
                "id": sessao["idSessao"],
                "title": sessao["tituloSessao"],
                "trainingBlocks": [],
            }
        bloco = {
            "id": sessao["idBlocoTreino"],
            "title": sessao["tituloBlocoTreino"],
            "linkedTraining": {
                "id": sessao["idTreino"],
                "title": sessao["tituloTreino"],
            },
        }
        sessoes_dict[sessao_id]["trainingBlocks"].append(bloco)

    planilha["sessions"] = list(sessoes_dict.values())

    return planilha
