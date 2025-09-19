# By default, request bodies are objects with predefined field names
# But we can declare the body as a plain dict if we don't want to specify key/value types

from fastapi import FastAPI

app = FastAPI

@app.post("/index-weights")
async def create_index_weights(weights: dict[int, float]):
    return weights
