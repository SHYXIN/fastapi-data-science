from fastapi import Body, FastAPI
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int

app = FastAPI()

@app.post("/users")
async def create_user(user: User, priority: int = Body(..., ge=1, le=3)):
    return {"user": user, "priority": priority}

# echo '{"user": {"name":"王鑫", "age": 30}, "priority":1}' | http POST http://localhost:8000/users

# http POST http://localhost:8000/users user:='{"name": "John", "age": 30}' priority=2
