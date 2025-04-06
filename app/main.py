from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api import routes
import uvicorn


app = FastAPI()
app.include_router(routes.router)
app.mount("/static", StaticFiles(directory="app/static"), name="static")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
