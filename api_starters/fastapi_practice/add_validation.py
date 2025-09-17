# Query lets you add extra validation (e.g. max len) to query parameters
# Annotaded combines types with validation

from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# q is optional, if provided, max length is 50
# Query with default value
# q: Annotated[str, Query()] = "ted"