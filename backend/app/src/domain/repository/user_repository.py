from sqlalchemy.orm import Session
from app.src.domain.model.user import User
from app.src.domain.dto.user_dto import CreateUser, UpdateUser

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_users(self):
        return self.session.query(User)
    
    def get_user_by_id(self, user_id: int):
        return self.session.query(User).filter(User.id == user_id).first()
    
    def get_user_by_email(self, user_email: str):
        return self.session.query(User).filter(User.email == user_email).first()
    
    def get_all_users(self):
        return self.session.query(User).all()
    
    def create_user(self, data: CreateUser, hashed_password: str) -> User:
        user = User(
            name=data.name, 
            email=data.email, 
            password_hash=hashed_password
        )
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
    
    def update_user(self, user_id, user_changes):
        user = self.session.query(User).filter(User.id == user_id).first()

        if user_changes.name:
            user.name = user_changes
        if user_changes.email:
            user.email = user_changes.email
        
        self.session.commit()
        self.session.refresh(user)
        return user
    
    def update_password(self, user_id, new_password_hash):
        user = self.session.query(User).filter(User.id == user_id).first()

        user.password_hash = new_password_hash
        self.session.commit()

        return True 
    
    def delete_user(self, user_id):
        user = self.session.query(User).filter(User.id == user_id).first()

        self.session.delete(user)
        self.session.commit()

        return True