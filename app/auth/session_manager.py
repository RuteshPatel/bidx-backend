from sqlalchemy.orm import Session

from app.auth.auth_utils import generate_session_token
from app.models.user_session import UserSession
from app.repository.session_repository import SessionRepository


def create_session(db: Session, user_id: int, role: str, device: str = None, ip: str = None):
    # deactivate old sessions for this user
    repo = SessionRepository(db)
    repo.deactivate_old_sessions(user_id)

    token = generate_session_token()

    session = UserSession(
        user_id=user_id,
        token=token,
        role=role,
        device_info=device,
        ip_address=ip
    )

    db.add(session)
    db.commit()
    db.refresh(session)

    return session


def validate_session(db: Session, token: str):
    return db.query(UserSession).filter(
        UserSession.token == token,
        UserSession.is_active == True
    ).first()


def logout_session(db: Session, token: str):
    db.query(UserSession).filter(
        UserSession.token == token
    ).update({"is_active": False})

    db.commit()
