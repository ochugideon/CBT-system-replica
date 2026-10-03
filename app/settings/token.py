from datetime import timedelta, datetime, timezone

from jose import jwt, JWTError

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/exam-login")

SECRET_KEY = '1234567890POIUYTREWQ'
ALGORITHM = 'HS256'
EXPIRE_MINUTES = 2

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
  
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        reg_number: str = payload.get("reg_number")
        access_code: str = payload.get("access_code")
        if access_code is None:
            return 'no access code'
        
        return {"reg_number": reg_number}
    except JWTError:
        return 'error'
        