# If we have a group of query parameters that are related, we can
# use a Pydantic model to represent them
# This keeps our code clean and reusable

from typing import Annotated, Literal 

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()

class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}  # forbid extra fields

    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []

@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query


# Libraries:
# Annotated = extra metadata, Literal = restrict allowed values
# BaseModel = model with validation, Field = extra validation/metadata

# URL: http://127.0.0.1:8000/items/?limit=10&offset=5&order_by=updated_at&tags=python&tags=fastapi

