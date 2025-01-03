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


def test_get_movimentos_by_professor():
    url = f"{BASE_URL}/movimentos/1"
    response = requests.get(url)
    if response.status_code == 200:
        print("Dados:")
        print(response.json())
    else:
        print(f"Status: {response.status_code}")
        print(response.text)


def test_get_movimento_by_id():
    url = f"{BASE_URL}/movimento/1/1"
    response = requests.get(url)
    if response.status_code == 200:
        print("Dados:")
        print(response.json())
    else:
        print(f"Status: {response.status_code}")
        print(response.text)


def test_get_modelos():
    url = f"{BASE_URL}/planilha/modelos/1"
    response = requests.get(url)
    if response.status_code == 200:
        print("Dados:")
        print(response.json())
    else:
        print(f"Status: {response.status_code}")
        print(response.text)


def test_get_planilha_by_id():
    url = f"{BASE_URL}/planilha/1"
    response = requests.get(url)
    if response.status_code == 200:
        print("Dados:")
        print(response.json())
    else:
        print(f"Status: {response.status_code}")
        print(response.text)


def test_vincular_planilha_a_aluno():
    url = f"{BASE_URL}/planilha/1/vincular"
    data = {
        "idProfessor": 1,
        "dataInicio": "2024-03-01",
        "dataFim": "2024-03-31",
        "alunos": [1, 2, 3],
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Dados:")
        print(response.json())
    else:
        print(f"Status: {response.status_code}")
        print(response.text)


def test_get_aluno_by_firebase_id():
    url = f"{BASE_URL}/aluno/JXoTjzg0rJf7AEBAkZVb7zgIJP53"
    response = requests.get(url)
    if response.status_code == 200:
        print("Dados:")
        print(response.json())
    else:
        print(f"Status: {response.status_code}")
        print(response.text)


def test_get_planilha_ativa_by_aluno():
    url = f"{BASE_URL}/aluno/1/planilha"
    response = requests.get(url)
    if response.status_code == 200:
        print("Dados:")
        print(response.json())
    else:
        print(f"Status: {response.status_code}")
        print(response.text)


def test_get_bloco_by_id():
    url = f"{BASE_URL}/bloco/15"
    response = requests.get(url)
    if response.status_code == 200:
        print("Dados:")
        print(response.json())
    else:
        print(f"Status: {response.status_code}")
        print(response.text)


if __name__ == "__main__":
    # Chamar as funções de teste
    test_get_bloco_by_id()
