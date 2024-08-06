from fastapi import Body, FastAPI, HTTPException, status


app = FastAPI()

@app.post("/password")
async def check_password(password: str = Body(...), password_confirm: str = Body(...)):
    if password != password_confirm:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail={
                "message": "Password don't match.",
                "hints": [
                    "Check the cpas lock on your keyborad",
                    "Try to make the password visible by clicking on the eye icon to check your typing.",
                ]
            }
        )
    return {"message": "Password match."}
