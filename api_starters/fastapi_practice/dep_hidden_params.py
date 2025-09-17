# deprecated=True -> marks a parameter as outdated but still usable  
# include_in_schema=False -> hides a parameter from the docs but keeps it functional  

from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    q: Annotated[str | None, Query(deprecated=True)] = None, 
    hidden: Annotated[str | None, Query(include_in_schema=False)] = None
):
    result = {"items": ["Black", "White"]}
    if q:
        result.update({"q": q})
    if hidden:
        result.update({"hidden": hidden})
    return result


