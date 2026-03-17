from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.src.infra.database import get_db
from app.src.infra.security.jwt_service import jwt_auth
from app.src.domain.service.user_service import UserService
from app.src.domain.dto.user_dto import CreateUser, UpdateUser, ReponseUser

router = APIRouter(prefix="/users")

@router.post("", response_model=ReponseUser, status_code=201)
def create_user(data: CreateUser, session: Session = Depends(get_db)):
    return UserService(session).create_user(data)

@router.get("", response_model=list[ReponseUser])
def get_users(session: Session = Depends(get_db)):
    return UserService(session).get_users()

@router.get("/{id}", response_model=ReponseUser)
def get_user_by_id(user_id: int = Depends(jwt_auth), session: Session = Depends(get_db)):
    return UserService(session).get_user_by_id(user_id)

@router.put("", response_model=ReponseUser)
def update_user(data: UpdateUser, user_id: int = Depends(jwt_auth), session: Session = Depends(get_db)):
    return UserService(session).update_user(user_id, data)

@router.delete("", status_code=204)
def delete_user(user_id: int = Depends(jwt_auth), session: Session = Depends(get_db)):
    return UserService(session).delete_user(user_id)