# Can use list as query parameter
# Must wrap list with Query(), otherwise FastAPI treats it as request body

from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[list[str] | None, Query()] = None):
    query_items = {"q": q}
    return query_items

# URL: http://localhost:8000/items/?q=foo&q=bar

# Can also define a default list of values 
# async def read_items(q: Annotated[list[str], Query()] = ["foo", "bar"])

# Use plain list: no type validation for elements
# async def read_items(q: Annotated[list, Query()] = [])