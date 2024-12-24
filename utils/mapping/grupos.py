import json


def map_grupos_by_professor_response(dados):
    grupos = []

    for grupo_id, grupo_nome, subgrupos_json in dados:
        subgrupos = json.loads(subgrupos_json)

        grupo = {"id": grupo_id, "nome": grupo_nome, "subGrupos": subgrupos}

        grupos.append(grupo)

    return grupos
