# Allows query names not valid in Python (e.g. user-id)
# Used to show a different name in the URL than in the function signature

from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(user_id: Annotated[str | None, Query(alias="user-id")] = None):
    if user_id:
        return {"user_id": user_id}
    return {"message": "No user ID provided"}

