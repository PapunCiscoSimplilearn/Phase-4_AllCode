# Employee OpenAPI First

A FastAPI employee API generated from `openapi.yaml`, with an in-memory implementation.

## Run

From the `employee-openapi-first` directory, create a virtual environment and install dependencies:

```bash
cd generated-server
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

Start the server:

```bash
python -m uvicorn openapi_server.main:app --app-dir src --reload --port 8000
```

Open http://127.0.0.1:8000/docs to try the API. Press Ctrl+C to stop the server. Run `deactivate` to leave the virtual environment.

`GET /employees` lists employees and `POST /employees` creates one. Data is held in memory and resets when the server restarts.

## Test

From `generated-server`, with the virtual environment activated:

```bash
PYTHONPATH=src python -m unittest discover -s tests -p test_employee_api.py -v
```

From the project directory, `make validate` checks the OpenAPI specification using Node.js and npx.

## Generation

The server was generated with OpenAPI Generator 7.12.0. Docker can run the generator from the project directory:

```bash
docker run --rm \
  -v "$PWD:/local" \
  openapitools/openapi-generator-cli:v7.12.0 generate \
  -i /local/openapi.yaml \
  -g python-fastapi \
  -o /local/generated-server
```

Regeneration can overwrite changes to generated files, including the POST status and required request body in the router, the Python 3.12-compatible `ujson` requirement, and the endpoint tests. Review and restore those changes after regenerating. The implementation is in `generated-server/src/openapi_server/impl/employee_api_impl.py`.