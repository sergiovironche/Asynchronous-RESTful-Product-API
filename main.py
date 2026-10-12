from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.v1.endpoints.products import router as products_router
from app.core.database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(
    title="Asynchronous RESTful Product API",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(products_router)

@app.get("/", tags=["Health"])
async def root():
    return {"message": "Async RESTful Product API is running."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)