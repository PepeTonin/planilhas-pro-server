import enum
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class SituacaoPagamentoEnum(str, enum.Enum):
    ativo = "ativo"
    inativo = "inativo"
    atrasado = "atrasado"


class SituacaoTreinoEnum(str, enum.Enum):
    regular = "regular"
    pendente = "pendente"
    requer_suporte = "requer suporte"


class AlunoBase(BaseModel):
    nome: str
    email: EmailStr
    dataNascimento: Optional[datetime] = None
    situacaoPagamento: SituacaoPagamentoEnum = SituacaoPagamentoEnum.ativo
    situacaoTreino: SituacaoTreinoEnum = SituacaoTreinoEnum.regular
    professorId: int


class AlunoCreate(AlunoBase):
    senha: str


class AlunoOut(AlunoBase):
    alunoId: int
    dataCadastro: datetime

    class Config:
        orm_mode = True
