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
        if sessao["idBlocoTreino"] is not None:
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


def map_planilha_ativa_by_aluno_response(dados):
    planilha_aluno = {
        "idPlanilha": dados[0]["idPlanilha"],
        "sessoes": [],
    }

    sessoes_dict = {}

    for sessao in dados:
        sessao_id = sessao["idSessao"]
        if sessao_id not in sessoes_dict:
            sessoes_dict[sessao_id] = {
                "idSessao": sessao["idSessao"],
                "tituloSessao": sessao["tituloSessao"],
                "blocos": [],
            }
        bloco = {
            "idBloco": sessao["idBlocoTreino"],
            "tituloBloco": sessao["tituloBlocoTreino"],
            "treino": {
                "idTreino": sessao["idTreino"],
                "tituloTreino": sessao["tituloTreino"],
            },
        }
        sessoes_dict[sessao_id]["blocos"].append(bloco)

    planilha_aluno["sessoes"] = list(sessoes_dict.values())

    return planilha_aluno


def map_bloco_by_id_response(dados, idBloco: str):
    movimentos = {}
    for movimento in dados:
        movimento_id = movimento["movimentoId"]
        if movimento_id not in movimentos:
            movimentos[movimento_id] = {
                "idMovimento": movimento_id,
                "tituloMovimento": movimento["tituloMovimento"],
                "descricoes": [],
            }
        movimentos[movimento_id]["descricoes"].append(movimento["descricaoMovimento"])

    detalhes_bloco_treino = {
        "idBloco": idBloco,
        "idTreino": dados[0]["treinoId"],
        "movimentos": list(movimentos.values()),
    }

    return detalhes_bloco_treino


def map_historico_planilhas_by_aluno_response(dados):
    historico = []
    for planilha in dados:
        historico.append(
            {
                "idPlanilha": planilha["planilhaId"],
                "dataInicio": planilha["dataInicio"],
                "dataFim": planilha["dataFim"],
            }
        )
    return historico
