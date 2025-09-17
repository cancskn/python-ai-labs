# This example shows how to get parameters from the path of the URL

from fastapi import FastAPI

app = FastAPI()

# basic path param
@app.get("/items/{item_id}") 
async def read_item(item_id): 
    return {"item_id": item_id} 

# url: http://127.0.0.1:8000/items/foo
# response: {"item_id": "foo"}


# path param with type
@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}

# http://127.0.0.1:8000/users/3 
# response: {"user_id": 3} parsed as int

