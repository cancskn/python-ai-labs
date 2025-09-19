# Query params = values passed in the URL after "?" like ?skip=1&limit=2

from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# skip: int = 0 -> take everything from the start
# limit: int = 10 -> take 10 items

# You can declare optional query parameters, by setting their default to None


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {
                "description": "This is an amazing item that has a long description"
            }
        )
    return item

# q: str | None = None -> optional query parameter
# short: bool = False -> boolean query parameter

# http://127.0.0.1:8000/items/foo?short=1      # True
# http://127.0.0.1:8000/items/foo?short=True   # True
# http://127.0.0.1:8000/items/foo?short=true   # True
# http://127.0.0.1:8000/items/foo?short=on     # True
# http://127.0.0.1:8000/items/foo?short=yes    # True
