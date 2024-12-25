import requests

BASE_URL = "http://localhost:8000/api/v1"


def test_get_grupo():
    url = f"{BASE_URL}/grupos/1"
    response = requests.get(url)
    if response.status_code == 200:
        print("Dados:")
        print(response.json())
    else:
        print(f"Status: {response.status_code}")
        print(response.text)


def test_login_professor():
    url = f"{BASE_URL}/login/professor"
    data = {"email": "carlos.silva@exemplo.com", "senha": "senha123"}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Dados:")
        print(response.json())
    else:
        print(f"Status: {response.status_code}")
        print(response.text)


def test_create_grupo():
    url = f"{BASE_URL}/novo/grupo"
    data = {"nome": "Grupo TESTE", "idProfessor": 1}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Dados:")
        print(response.json())
    else:
        print(f"Status: {response.status_code}")
        print(response.text)


def test_create_subgrupo():
    url = f"{BASE_URL}/novo/subgrupo"
    data = {"nome": "Subgrupo TESTE", "idGrupo": 1}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Dados:")
        print(response.json())
    else:
        print(f"Status: {response.status_code}")
        print(response.text)


def test_create_treino():
    url = f"{BASE_URL}/treino/novo"
    data = {
        "idProfessor": 1,
        "titulo": "titulo treino",
        "descricao": "descricao treino",
        "movimentos": [
            {
                "id": 1,
                "titulo": "movimentoA",
                "descricoes": [
                    {"id": 1, "descricao": "descricao1"},
                    {"id": 2, "descricao": "descricao2"},
                ],
            },
            {
                "id": 2,
                "titulo": "easas",
                "descricoes": [
                    {"id": 3, "descricao": "descricao1"},
                    {"id": 4, "descricao": "descricao2"},
                ],
            },
        ],
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Dados:")
        print(response.json())
    else:
        print(f"Status: {response.status_code}")
        print(response.text)


if __name__ == "__main__":
    # Chamar as funções de teste
    test_create_treino()