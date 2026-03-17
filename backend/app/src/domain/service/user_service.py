from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.src.domain.repository.user_repository import UserRepository
from app.src.domain.dto.user_dto import CreateUser, UpdateUser
from app.src.infra.security.encryption_service import EncryptionService

class UserService:
    def __init__(self, session: Session):
        self.user_repository = UserRepository(session)
        self.encryption_service = EncryptionService()

    def create_user(self, data: CreateUser):
        if self.user_repository.get_user_by_email(data.email):
            raise HTTPException(
                status_code=400,
                detail="E-mail já cadastrado"
            )
        return self.user_repository.create_user(data, self.encryption_service.hash_password(data.password))
        
    def get_users(self):
        return self.user_repository.get_all_users()
    
    def get_user_by_id(self, user_id: int):
        user = self.user_repository.get_user_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=404,
                detail="Usuário não encontrado"
            )
        return user
    
    def get_user_by_email(self, email: str):
        user = self.user_repository.get_user_by_email(email)
        if not user:
            raise HTTPException(
                status_code=404, 
                detail="Usuário não encontrado"
            )
        return user
    
    def update_user(self, user_id: int, data: UpdateUser):
        user = self.user_repository.get_user_by_id(user_id)
        if data.email and self.user_repository.get_user_by_email(data.email):
            raise HTTPException(
                status_code=400,
                detail="E-mail já em uso"
            )
        return self.user_repository.update_user(user, data)
    
    def delete_user(self, user_id: int):
        user = self.user_repository.get_user_by_id(user_id)
        self.user_repository.delete_user(user)