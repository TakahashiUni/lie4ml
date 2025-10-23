from fastapi import FastAPI

app = FastAPI(title="Lie4ML Backend", version="0.1")


@app.get("/api/v1/hello")
async def hello():
    return {"message": "Hello World!"}
