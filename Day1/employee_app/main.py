from fastapi import FastAPI

from database.connection import Base, engine
from routers.employee_router import router as employee_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
	title="Employee Management API",
	description="FastAPI application using layered architecture",
	version="1.0.0",
)
app.include_router(employee_router)


@app.get("/")
def home():
	return {"message": "Welcome to Employee Management API"}
