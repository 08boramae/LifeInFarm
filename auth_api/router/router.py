from fastapi import APIRouter, Form, Response, status, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from database.handle_database import *
from datetime import datetime, timedelta, timezone
from model.model import *
import jwt
from typing import Annotated

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = "verysecret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get('id')
        if user_id is None:
            raise credentials_exception
    except:
        raise credentials_exception

    user_data = get_user_by_username(user_id)
    if user_data is None:
        raise credentials_exception
    user = User(id=user_data[0], name=user_data[1], location=user_data[2])
    return user


@router.post('/login')
async def _login(response: Response, data: OAuth2PasswordRequestForm = Depends()):
    user = login(data.username, data.password)
    if user:
        response.status_code = status.HTTP_200_OK
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"uid": user[0], "id": user[1], "name": user[2]},
            expires_delta=access_token_expires
        )
        return {"code": 201, "message": "success", "access_token": access_token, "token_type": "bearer"}
    else:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"code": 500, "message": "Internal server error"}


@router.post('/register')
async def register(data: Annotated[AddUserRequest, Form()], response: Response):
    if add_user(data.id, data.name, data.pw, data.location, ):
        response.status_code = status.HTTP_201_CREATED
        return {"code": 201, "message": "success"}
    else:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"code": 500, "message": "Internal server error"}


@router.get('/oauth2/authorize')
async def authorize():
    # TODO
    return 0


@router.post('/oauth2/authorize')
async def post_authorize():
    # TODO
    return 0


@router.get('/oauth2/token')
async def get_token():
    # TODO
    return 0


@router.delete('/oauth2/token')
async def delete_token():
    # TODO
    return 0


@router.patch('/oauth2/token')
async def patch_token():
    # TODO
    return 0


@router.get('/@me', response_model=User)
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)], ):
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return current_user
