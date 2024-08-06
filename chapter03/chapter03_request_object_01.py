from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def get_request_object(request: Request):
    return {"path": request.url.path}


#  http -v GET http://localhost:8000
