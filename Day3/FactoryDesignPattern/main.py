from fastapi import FastAPI, HTTPException

from factory_demo import EmployeeService, RepositoryFactory


app = FastAPI()


@app.get("/employees/{db_type}")
def get_employees(db_type: str):
    try:
        repository = RepositoryFactory.create_repository(db_type)
        service = EmployeeService(repository)
        return {"database": db_type, "employees": service.get_employees()}
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error