# body, path and query parameters can be declared together

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.put("/items/{item_id}") 
async def update_item(item_id: int, item: Item, q: str | None = None): 
    result = {"item_id": item_id, **item.model_dump()} 
    if q:
        result.update({"q": q})
    return result

# item_id: path parameter
# item: body parameter
# q: query parameter