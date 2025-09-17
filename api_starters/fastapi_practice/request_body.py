# Request body means the data sent by the client to your API
# Pydantic model is used 
# Client: Browser, Mobile App, etc.
# POST, PUT, DELETE, PATCH

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item): # item: request body
    item_dict = item.model_dump()  # same as dict, it does not supported in Pydantic v2
    if item.tax is not None:
        total_price = item.price + item.tax
        item_dict.update({"total_price": total_price})
    return item_dict