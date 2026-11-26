class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("Database connection object created")
        return cls._instance

    def connect(self):
        print("Connected to database")


db1 = DatabaseConnection()
db2 = DatabaseConnection()
db3 = DatabaseConnection()

db1.connect()
db2.connect()

print(db1 is db2)
print(db2 is db3)

print(id(db1))
print(id(db2))
print(id(db3))