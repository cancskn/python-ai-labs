# Custom validation allows to define your own rules beyond the built-in validators
# BeforeValidator runs your custom function before the built-in validation steps  
# AfterValidator runs your custom function after the built-in validation steps

import random
from typing import Annotated
from fastapi import FastAPI
from pydantic import BeforeValidator, AfterValidator

app = FastAPI()

data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}

def normalize_id(id: str):
    # Converts input to lowercase before validation
    return id.lower()

def check_valid_id(id: str):
    # Ensures the value starts with isbn or imdb
    if not id.startswith(("isbn", "imdb")): # tuple for multiple options
        raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
    return id

@app.get("/items/")
async def read_item(
    id: Annotated[str | None, BeforeValidator(normalize_id), AfterValidator(check_valid_id)] = None,
):
    if id:
        item = data.get(id)
    else:
        id, item = random.choice(list(data.items()))
    return {"id": id, "name": item}


# Explanation of id, item = random.choice(list(data.items())):

# data.items() -> returns a dict_items view of (key, value) tuples
# dict_items([("imdb-tt0371724", "The Hitchhiker's Guide to the Galaxy"), ...])

# list(data.items()) -> converts the dict_items view to a list of tuples
# [("imdb-tt0371724", "The Hitchhiker's Guide to the Galaxy"), ...]

# random.choice(list(...)) -> picks one random (key, value) tuple from the list

# id, item = ... -> unpacks the selected tuple into id and item variables