from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "sua resposta"}

@app.get("/teste")
def read_teste():
    return {"message": "Bom dia, boa tarde, boa noite!"}


