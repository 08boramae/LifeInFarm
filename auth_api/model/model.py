from pydantic import BaseModel

class LoginRequest(BaseModel):
    id: str
    password: str

class AddUserRequest(BaseModel):
    id: str
    name: str
    pw: str
    location: str

class Token(BaseModel):
    access_token: str
    token_type: str

class User(BaseModel):
    id: int
    name: str
    location: str

class TokenData(BaseModel):
    username: str | None = None