from fastapi import APIRouter
from dependency_injector.wiring import inject

app_router = APIRouter()
@app_router.get("/hello_world/")
@inject
async def hello():
    """
    hello world endpoint
    """
    return("hello world")