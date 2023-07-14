from datetime import datetime
from typing import List, Union
from pydantic import BaseModel



class NoteBase(BaseModel):
    title: str
    content: Union[str, None] = None
    category: Union[str, None] = None 
    published: bool = False
    createdAt: datetime 
    updatedAt: datetime 

class NoteCreate(NoteBase):
    pass  

class NoteUpdate(NoteBase):
    pass  

class Note(NoteBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None

class ApiKeyBase(BaseModel):
    key: str

class ApiKey(ApiKeyBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class ApiKeyCreate(ApiKeyBase):
    pass


class UserBase(BaseModel):
    username: str
    email: Union[str, None] = None

class UserCreate(UserBase):
    password: str

class User(BaseModel):
    username: str
    email: Union[str, None] = None
    is_active: Union[bool, None] = None
    api_keys: List[ApiKey] = []
    notes: List[Note] = []

    class Config:
        orm_mode = True


class DateTime(BaseModel):
    Day: str
    Month: str
    Year: str
    Time: str