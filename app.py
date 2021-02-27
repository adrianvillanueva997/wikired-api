from fastapi import FastAPI

from src.services.sv_wikired import Wikired

app = FastAPI()
wikired = Wikired()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/ukranian")
async def get_ukranian():
    text = await wikired.ukranian()
    return {"text": text}


@app.get("/wikired")
async def get_wikired():
    text = await wikired.wikired()
    return {"text": text}
