# Non-Annotated (order matters)
# Here q is required (no default), item_id uses path (looks like default)
# Python requires that non-defaults come before defaults

from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/items-non-annotated/{item_id}")
async def read_item_non_annotated(
    q: str,
    item_id: int = Path(..., title="The ID of the item to get"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# Annotated (order does not matter)
# with Annotated, FastAPI knows from metadata, so Pyhton doesn't complain

@app.get("/items-annotated/{item_id}")
async def read_items_annotated(item_id: Annotated[int, Path(title="The ID of the item to get")], q: str):
    return {"q": q, "item_id": item_id}

# In the URL: path parameters are ordered and fixed, query parameters are order-independent  
