from fastapi import FastAPI
from app.routes import auth, tasks
from fastapi.openapi.utils import get_openapi


app = FastAPI()

app.include_router(auth.router)
app.include_router(tasks.router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

