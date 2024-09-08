from pydantic import BaseModel


class UserSignupSchema(BaseModel):
    name: str
    email: str
    password: str

class UserLoginSchema(BaseModel):
    email: str
    password: str

class UserResponseSchema(BaseModel):
    id: str
    name: str
    email: str
    token: str = None