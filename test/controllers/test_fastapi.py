import pytest
from fastapi import FastAPI

# Resources.:  https://fastapi.tiangolo.com/tutorial/first-steps/

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}