from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/")
async def custom_cookie(response: Response):
    response.set_cookie("cookie-name", "cookie-value", max_age=86400)
    response.set_cookie(key="session_token", value="abc123")
    return {"hello": "world"}


@app.get('/set-cookie')
async def custom_cookie2(response: Response):
    response.headers['Set-Cookie'] = "username=JohnDoe; Path=/set-cookie; HttpOnly"
    response.headers['Set-Cookie'] += ", session_token=abc123; Path=/; HttpOnly"
    return {"message": "Cookie has been set"}
