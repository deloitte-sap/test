
from fastapi import FastAPI
from app.routers import example_router, prediction_router

app = FastAPI()

app.include_router(example_router.router)
app.include_router(prediction_router.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
