import uvicorn
from fastapi import FastAPI

from .routers.categories import router as categories_router
from .routers.notes import router as notes_router

HOST = '127.0.0.1'
PORT = 8000

app = FastAPI()

app.include_router(notes_router)
app.include_router(categories_router)

if __name__ == '__main__':
    uvicorn.run(app, host=HOST, port=PORT)
