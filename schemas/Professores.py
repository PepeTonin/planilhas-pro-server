from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class ProfessorBase(BaseModel):
    nome: str
    email: EmailStr


class ProfessorCreate(ProfessorBase):
    senha: str


class ProfessorOut(ProfessorBase):
    professorId: int
    dataCadastro: datetime
    ativo: bool
