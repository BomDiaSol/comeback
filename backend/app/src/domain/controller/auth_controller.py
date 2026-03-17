from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.src.domain.dto.login_data import LoginData
from app.src.domain.service.auth_service import AuthenticationService
from app.src.infra.database import get_db

router = APIRouter(prefix="/authentication")

@router.post("/login")
def login(login_data: LoginData, session: Session = Depends(get_db)):
    token = AuthenticationService(session).authenticate_user(login_data)
    return {"access_token": token, "token_type": "bearer"}