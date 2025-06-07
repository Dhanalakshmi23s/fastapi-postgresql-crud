from fastapi import FastAPI
from router import posts
from database import Base, engine
from router import files

Base.metadata.create_all(bind=engine)

app=FastAPI()

@app.get("/")
async def root():
    return{"message":"hello world"}

@app.get("/hello/{name}")
async def say_hello(name:str):
    return{"message":f"Hello {name}"}

app.include_router(posts.router)

app.include_router(files.router)

