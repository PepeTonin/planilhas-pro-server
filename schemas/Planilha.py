from typing import List
from pydantic import BaseModel


class BaseBloco(BaseModel):
    titulo: str
    idTreino: int


class BaseSessao(BaseModel):
    titulo: str
    blocos: List[BaseBloco]


class BodyRequestCreatePlanilha(BaseModel):
    idProfessor: int
    titulo: str
    descricao: str
    sessoes: List[BaseSessao]
