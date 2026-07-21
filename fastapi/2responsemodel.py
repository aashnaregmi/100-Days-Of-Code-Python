from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Fake Database
users = []


# Data user sends while creating an account
class UserCreate(BaseModel):
    id: int
    name: str
    age: int
    email: str
    password: str


# Data returned to the client
class UserResponse(BaseModel):
    id: int
    name: str
    age: int


# CREATE USER
@app.post("/users")
def create_user(user: UserCreate):
    users.append(user)
    return {"message": "User created successfully"}


# GET USER
@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return {"id": user.id, "name": user.name, "age": user.age}

    return {"message": "User not found"}
