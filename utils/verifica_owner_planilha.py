from db.service.planilhas import db_get_planilha_by_id


def verifica_owner_planilha(idProfessor: int, idPlanilha: int) -> bool:
    dados = db_get_planilha_by_id(idPlanilha)
    id_owner = dados[0]["professorId"]
    return id_owner == idProfessor
