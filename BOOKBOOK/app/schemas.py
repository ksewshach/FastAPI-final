from pydantic import BaseModel

class CreateUserSchema(BaseModel):
    username: str
    email: str
    password: str
    id: int

class ChapterCreateSchema(BaseModel):
    title: str
    description: str
    id: int

class ChapterUpdateSchema(BaseModel):
    title: str
    description: str


