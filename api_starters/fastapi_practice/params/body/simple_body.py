# By default, simple types are treated as query parameters
# Use Body() to force a simple type into the request body

from typing import Annotated
from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
async def create_item(item: Item, importance: Annotated[int, Body()]):
    return {"item": item, "importance": importance}

# importance: body parameter