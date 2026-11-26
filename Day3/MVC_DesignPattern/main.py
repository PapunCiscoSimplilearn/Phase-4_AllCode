from fastapi import FastAPI

from controllers.employee_controller import router


app = FastAPI(title="Employee Management System")
app.include_router(router)


@app.get("/")
def home():
    return {"message": "Welcome to MVC Application"}