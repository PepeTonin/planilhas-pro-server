from typing import List
from pydantic import BaseModel


class BaseDescricaoMovimento(BaseModel):
    id: int
    descricao: str


class BaseMovimento(BaseModel):
    id: int
    titulo: str
    descricoes: List[BaseDescricaoMovimento]


class BodyRequestCreateTreino(BaseModel):
    idProfessor: int
    titulo: str
    descricao: str
    movimentos: List[BaseMovimento]
