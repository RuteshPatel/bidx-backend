from fastapi import Depends, HTTPException
from app.middleware.auth_middleware import get_current_user


def require_super_admin(current_user=Depends(get_current_user)):
    if not current_user.get("role") == "super_admin":
        raise HTTPException(status_code=403, detail="You don't have enough privileges to perform this action")
    return current_user
