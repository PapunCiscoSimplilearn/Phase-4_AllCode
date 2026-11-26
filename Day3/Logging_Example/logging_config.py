import logging
from contextvars import ContextVar
from logging.handlers import RotatingFileHandler
from pathlib import Path


trace_id_var = ContextVar("trace_id", default="SYSTEM")


class TraceIDFilter(logging.Filter):
    def filter(self, record):
        record.trace_id = trace_id_var.get()
        return True


logs_directory = Path(__file__).resolve().parent / "logs"
logs_directory.mkdir(exist_ok=True)

logger = logging.getLogger("employee_app")
logger.setLevel(logging.DEBUG)
logger.propagate = False

if not logger.handlers:
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | TraceID=%(trace_id)s | "
        "%(filename)s:%(lineno)d | %(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    console_handler.addFilter(TraceIDFilter())

    file_handler = RotatingFileHandler(
        logs_directory / "application.log",
        maxBytes=1024 * 1024,
        backupCount=3,
        encoding="utf-8",
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(TraceIDFilter())

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)