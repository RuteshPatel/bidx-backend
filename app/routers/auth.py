from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.middleware.auth_middleware import get_current_user
from app.schemas.auth_schema import LoginRequest, LoginResponse
from app.services.auth_service import AuthService

router = APIRouter()
auth_service_obj = AuthService()


@router.post("/login", response_model=LoginResponse)
def login(payload: LoginRequest, request: Request, db: Session = Depends(get_db)):
    device = request.headers.get("User-Agent")
    ip = request.client.host
    return auth_service_obj.login(db, payload, device, ip)


@router.post("/logout")
def logout(current_session=Depends(get_current_user), db: Session = Depends(get_db)):
    auth_service_obj.logout(db, current_session.get('token'))
    return {"message": "Logged out successfully"}
