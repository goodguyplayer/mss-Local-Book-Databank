import pytest
from fastapi import FastAPI

# Resources.:  https://fastapi.tiangolo.com/tutorial/first-steps/

test = FastAPI()


@test.get("/")
async def root():
    return {"message": "Hello World"}

@test.get("/app/")
async def root():
    return {"message": "Dir changed"}

@test.get("/app/thisisatest")
async def root():
    return {"message": "Dir changed"}