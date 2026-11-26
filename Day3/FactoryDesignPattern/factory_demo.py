from abc import ABC, abstractmethod


class EmployeeRepository(ABC):
    @abstractmethod
    def get_employees(self):
        pass


class SQLiteRepository(EmployeeRepository):
    def get_employees(self):
        return [
            {"id": 101, "name": "Rahul", "db": "SQLite"},
            {"id": 102, "name": "Amit", "db": "SQLite"},
        ]


class MySQLRepository(EmployeeRepository):
    def get_employees(self):
        return [
            {"id": 201, "name": "John", "db": "MySQL"},
            {"id": 202, "name": "David", "db": "MySQL"},
        ]


class MongoDBRepository(EmployeeRepository):
    def get_employees(self):
        return [
            {"id": 301, "name": "Neha", "db": "MongoDB"},
            {"id": 302, "name": "Priya", "db": "MongoDB"},
        ]


class RepositoryFactory:
    @staticmethod
    def create_repository(db_type):
        if db_type == "sqlite":
            return SQLiteRepository()
        elif db_type == "mysql":
            return MySQLRepository()
        elif db_type == "mongodb":
            return MongoDBRepository()
        else:
            raise ValueError("Unsupported database")


class EmployeeService:
    def __init__(self, repository: EmployeeRepository):
        self.repository = repository

    def get_employees(self):
        return self.repository.get_employees()


if __name__ == "__main__":
    db_type = input("Enter database type: ")
    repository = RepositoryFactory.create_repository(db_type)
    service = EmployeeService(repository)
    print(service.get_employees())