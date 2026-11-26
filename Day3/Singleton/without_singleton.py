class DatabaseConnection:
    def __init__(self):
        print("Database connection object created")


db1 = DatabaseConnection()
db2 = DatabaseConnection()
db3 = DatabaseConnection()

print(db1 is db2)
print(db2 is db3)