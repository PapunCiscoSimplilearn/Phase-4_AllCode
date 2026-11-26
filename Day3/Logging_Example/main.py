import time
import uuid

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

from employee_service import EmployeeService
from logging_config import logger, trace_id_var


app = FastAPI(title="Employee Logging and Trace ID Example")
service = EmployeeService()


@app.middleware("http")
async def trace_id_middleware(request: Request, call_next):
    trace_id = uuid.uuid4().hex
    token = trace_id_var.set(trace_id)
    start_time = time.perf_counter()
    logger.info("Request started: %s %s", request.method, request.url.path)

    try:
        response = await call_next(request)
    except ConnectionError:
        logger.exception("Database service unavailable")
        response = JSONResponse(
            status_code=503,
            content={"message": "Service unavailable", "trace_id": trace_id},
        )
    except Exception:
        logger.exception("Unexpected application error")
        response = JSONResponse(
            status_code=500,
            content={"message": "Internal server error", "trace_id": trace_id},
        )
    finally:
        duration = (time.perf_counter() - start_time) * 1000
        logger.info("Request completed in %.2f ms", duration)
        trace_id_var.reset(token)

    response.headers["X-Trace-ID"] = trace_id
    return response


@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    logger.info("Controller received employee ID: %s", employee_id)
    employee = service.get_employee(employee_id)

    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return {"trace_id": trace_id_var.get(), "employee": employee}