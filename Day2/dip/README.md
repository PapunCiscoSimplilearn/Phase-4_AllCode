# Dependency Inversion Principle (DIP)

High-level and low-level modules should both depend on abstractions. Abstractions should not depend on implementation details.

## Database example

An `EmployeeService` that constructs `MySQLDatabase` directly is tied to MySQL. Switching databases requires changing the service.

Here, `EmployeeService` accepts a `Database` abstraction through its constructor. Both `MySQLDatabase` and `PostgreSQLDatabase` implement that abstraction, so either can be supplied without modifying the service. This reduces coupling, makes database replacement easier, and allows a test double to be injected for unit tests.

The example only prints messages; it does not connect to a real database.

Run the example from the workspace root:

```bash
python3 Day2/dip/main.py
```

Expected output:

```text
Saving data into MySQL
Saving data into PostgreSQL
```