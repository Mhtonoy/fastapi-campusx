from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {'message' : 'Hello world'}

@app.get("/about")
def hello():
    return {'message' : 'XYZ is an educational platform'}