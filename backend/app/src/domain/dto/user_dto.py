from pydantic import BaseModel, EmailStr
from typing import Optional

class CreateUser(BaseModel):
    name: str
    email: EmailStr # Eu vi que ele já verifica se o email é válido no formato blablabla@dominio.com
    password: str

class UpdateUser(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

class ReponseUser(BaseModel):
    id: int
    name: str
    email: str

    model_config = {'from_attributes': True}