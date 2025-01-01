from pydantic import BaseModel


class BodyRequestCreateAluno(BaseModel):
    firebaseId: str
    nome: str
    email: str
    senha: str


class BodyRequestVincularProfessorAluno(BaseModel):
    idProfessor: int
    idAluno: int
