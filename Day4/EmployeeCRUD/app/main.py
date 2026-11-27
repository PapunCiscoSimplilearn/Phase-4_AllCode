from fastapi import FastAPI

from app.routes import router

app = FastAPI(title="Employee CRUD API")
app.include_router(router)