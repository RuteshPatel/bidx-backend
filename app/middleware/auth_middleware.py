from fastapi import Request, HTTPException, Depends
from sqlalchemy.orm import Session

from app.auth.session_manager import validate_session
from app.core.database import get_db
from app.models.users import User


async def get_current_user(request: Request, db: Session = Depends(get_db)):
    auth_header = request.headers.get("Authorization")

    if not auth_header:
        raise HTTPException(status_code=401, detail="Missing token")

    token = auth_header.split(" ")[1]

    session = validate_session(db, token)

    if not session:
        raise HTTPException(status_code=401, detail="Invalid or expired session")

    user = db.query(User).filter(User.id == session.user_id).first()

    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    user_response = {
        "username": user.username,
        "email": user.email,
        "id": user.id,
        "phone": user.phone,
        "token": session.token,
    }
    return user_response
