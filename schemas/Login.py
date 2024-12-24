from pydantic import BaseModel, EmailStr


class BodyRequestLogin(BaseModel):
    email: EmailStr
    senha: str
