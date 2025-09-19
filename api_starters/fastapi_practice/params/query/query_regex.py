from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None, Query(min_length=3, max_length=50, regex="^a.*[rts].x$")
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# You can use default values instead of None
# async def read_items(q: Annotated[str, Query(min_length=3)] = "fixedquery")

# Required None: None can be a required value. This will force the user to provide a value, even if it's None
# async def read_items(q: Annotated[str | None, Query(min_length=3)])


# regex explanation:
# ^a - string must start with 'a'
# .*[rts] - followed by any of these characters, must include at least one
# .x$ - ends with 'x'