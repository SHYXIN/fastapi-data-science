from fastapi import FastAPI, Cookie

app = FastAPI()

@app.get("/")
async def get_cookie(hello: str | None = Cookie(None)):
    return {"hello": hello}

# 区分大小写
# http -v GET http://localhost:8000 Cookie:hello=World
# http -v GET http://localhost:8000 Cookie:hellO=World
