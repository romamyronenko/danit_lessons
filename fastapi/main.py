from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from starlette.responses import HTMLResponse

from funcs import cows_and_bulls


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(111)
    yield
    print(222)


app = FastAPI(lifespan=lifespan)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    print("aaa")
    response = await call_next(request)
    print("bb", response)
    return response


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/bulls_and_cows")
async def read_item(secret: str, guess: str):
    """
    My description
    """
    return cows_and_bulls(secret, guess)


@app.get("/html")
async def html():
    """My description

    :param secret some secret descr
    """
    return HTMLResponse("<h1>Hello,asdsasdadworld</h1>")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
