from fastapi import FastAPI
from app.src.infra.database import Base, engine
from app.src.domain.controller.auth_controller import router as auth_router
from app.src.domain.controller.user_controller import router as user_router

app = FastAPI(title="Comeback API")

app.include_router(user_router)
app.include_router(auth_router)