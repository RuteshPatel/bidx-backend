import base64
import hashlib
from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext

from app.core.config import SECRET_KEY, ALGORITHM

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password):
    pre_hash = hashlib.sha256(password.encode('utf-8')).digest()
    safe_input = base64.b64encode(pre_hash).decode('ascii')
    return pwd_context.hash(safe_input)


def verify_password(plain, hashed):
    pre_hash = hashlib.sha256(plain.encode('utf-8')).digest()
    safe_input = base64.b64encode(pre_hash).decode('ascii')
    return pwd_context.verify(safe_input, hashed)


def create_access_token(data):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=60)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
