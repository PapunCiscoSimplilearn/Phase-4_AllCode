from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base


DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/employee_db"


engine = create_engine(DATABASE_URL)


Base = declarative_base()
