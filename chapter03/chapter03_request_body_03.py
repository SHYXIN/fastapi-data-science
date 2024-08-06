from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int


class Company(BaseModel):
    name: str


app = FastAPI()


@app.post("/users")
async def create_user(user: User, company: Company):
    return {"user": user, "company": company}

# http POST http://localhost:8000/users user:='{"name": "John", "age": 30}' company:='{"name": "ACME"}'

# echo '{"user": {"name": "John", "age": 30}, "company": {"name": "ACEM"}}' | http POST http://localhost:8000/users
