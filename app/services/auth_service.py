from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.auth.session_manager import create_session, logout_session
from app.core.security import verify_password
from app.models.users import User
from app.schemas.auth_schema import LoginRequest


class AuthService:
    def login(self, db: Session, payload: LoginRequest, device, ip_address):
        user = db.query(User).filter(
            User.email == payload.email,
            User.is_active == True
        ).first()

        if not user:
            raise HTTPException(status_code=400, detail="Invalid credentials")

        if not verify_password(payload.password, user.password):
            raise HTTPException(status_code=400, detail="Invalid credentials")

        session = create_session(
            db=db,
            user_id=user.id,
            role=user.role.name,
            device=device,
            ip=ip_address
        )

        return {
            "access_token": session.token,
            "user_id": user.id,
            "role": user.role.name,
        }

    def logout(self, db: Session, token: str):
        logout_session(db, token)
        return {"message": "Logged out successfully"}
