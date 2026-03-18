from fastapi import FastAPI

import random

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "sua resposta"}

@app.get("/teste")
def read_teste():
    return {"numero": random.randint(0, 100)}


