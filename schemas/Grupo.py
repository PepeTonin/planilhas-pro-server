from pydantic import BaseModel


class BodyRequestInsertGrupo(BaseModel):
    idProfessor: int
    nome: str


class BodyRequestInsertSubGrupo(BaseModel):
    nome: str
    idGrupo: int
