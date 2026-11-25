from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass


class MySQLDatabase(Database):
    def save(self, data):
        print("Saving data into MySQL")


class PostgreSQLDatabase(Database):
    def save(self, data):
        print("Saving data into PostgreSQL")


class EmployeeService:
    def __init__(self, database: Database):
        self.database = database

    def save_employee(self, employee):
        self.database.save(employee)


def main():
    mysql_service = EmployeeService(MySQLDatabase())
    mysql_service.save_employee("Irfan")

    postgres_service = EmployeeService(PostgreSQLDatabase())
    postgres_service.save_employee("Irfan")


if __name__ == "__main__":
    main()