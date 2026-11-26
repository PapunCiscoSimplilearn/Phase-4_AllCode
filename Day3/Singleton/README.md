# Singleton Design Pattern

Singleton is a creational design pattern that ensures a class has one instance within a process and provides a common access point to it. Common uses include application configuration, logging, database connection pool managers, caches, and resource managers.

## Python examples

Run these commands from this directory:

```bash
python3 without_singleton.py
python3 singleton_demo.py
```

Without Singleton, each construction creates a separate object, so both identity comparisons are `False`. With Singleton, the object is created once, both comparisons are `True`, and all three printed object IDs are equal. The actual IDs vary between runs.

In the Singleton example, `_instance` stores the instance, and `__new__` controls object creation. It checks whether the instance exists, creates it using `super().__new__(cls)` if needed, and returns the stored instance.

## FastAPI example

Install the dependencies and start the application from this directory:

```bash
python3 -m pip install -r requirements.txt
uvicorn main:app --reload
```

Open http://127.0.0.1:8000/docs and try `GET /employees` and `GET /departments`. Both responses contain the same `object_id` when handled by the same process.

This is a simplified demonstration with dummy database logic. It is not thread-safe. Production applications should use appropriate synchronization or FastAPI lifespan management with a database connection pool. Each Uvicorn worker process has its own instance.