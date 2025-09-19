# Here ge=1 means item_id should be greater than or equal to 1
from typing import Annotated
from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=1)],
    q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

@app.get("/products/{product_id}")
async def read_product(
    product_id: Annotated[int, Path(title="The ID of the product to get", ge=1, le=10)],
    q: str,
    size: Annotated[float, Query(gt=0, lt=10.5)],
):
    results = {"product_id": product_id}
    if q:
        results.update({"q": q})
    if size:
        results.update({"size": size})
    return results

# ge: greater than or equal
# gt: greater than
# le: less than or equal
# lt: less than

# URL: http://127.0.0.1:8000/items/12?q=book
# URL: http://127.0.0.1:8000/products/15?q=laptop&size=5.5
