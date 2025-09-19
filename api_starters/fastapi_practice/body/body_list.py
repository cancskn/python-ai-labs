# FastAPI allows to declare body as a pure list

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str

@app.post("/images/multiple/")
async def create_multiple_images(images: list[Image]):
    return images

# Example body:
# [
#   {
#     "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png",
#     "name": Logo1  
#   },
#   {
#     "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png",
#     "name": Logo2
#   }
# ] 
