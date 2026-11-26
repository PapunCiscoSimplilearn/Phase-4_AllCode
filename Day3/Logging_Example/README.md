# FastAPI Logging with Trace IDs

This example logs employee requests at DEBUG, INFO, WARNING, ERROR, and CRITICAL levels. A request-scoped `ContextVar` carries one trace ID through the controller, service, repository, and log handlers. The ID is returned in the `X-Trace-ID` response header; successful and server-error JSON responses also include it in the body.

Logs are written to the console and to `logs/application.log`. The file rotates at 1 MiB and retains three backups. The repository uses in-memory sample records; IDs 500 and 999 intentionally simulate a database query error and unavailable database service.

## Run

From this directory, create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows, use `python -m venv .venv` and `.venv\\Scripts\\activate` instead. Install the dependencies and start the server:

```bash
python -m pip install -r requirements.txt
uvicorn main:app --reload
```

Open `http://127.0.0.1:8000/docs` to try the endpoint.

## Scenarios

| Request | Expected status | Behavior |
| --- | ---: | --- |
| `GET /employees/101` | 200 | Employee returned; DEBUG and INFO logs |
| `GET /employees/105` | 404 | Employee missing; WARNING log |
| `GET /employees/500` | 500 | Simulated query failure; exception traceback logged at ERROR |
| `GET /employees/999` | 503 | Simulated database outage; CRITICAL and ERROR logs |

Every response includes an `X-Trace-ID` header. The 200, 500, and 503 JSON bodies also include `trace_id`. The 404 uses FastAPI's standard `{"detail":"Employee not found"}` body.