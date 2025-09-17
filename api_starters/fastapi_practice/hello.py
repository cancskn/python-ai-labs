from fastapi import FastAPI

app = FastAPI() # Instance of FastAPI

@app.get("/")  # Decorator for GET request at root URL
async def root(): # Define async function for root endpoint
    return {"message": "Hello World"}
