from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/users")
async def get_user(page: int = Query(1, gt=0), size: int = Query(10, le=100)):
    return {"page": page, "size": size}


# http "http://localhost:8000/users"

#  http "http://localhost:8000/users?size=1000"
