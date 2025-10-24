from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import articles, users

app = FastAPI(title="Lie4ML Backend", version="0.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def hello():
    return {"message": "Hello World!"}

app.include_router(articles.router, prefix="/api/v1")
app.include_router(users.router, prefix="/api/v1")