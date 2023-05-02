from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine, select


Database = 'sqlite:///data/eksamen_database.db'
Base = declarative_base()


def set_sqlite_pragma(dbapi_connection, connection_record):
   cursor = dbapi_connection.cursor()
   cursor.execute("PRAGMA foreign_keys=ON")
   cursor.close()


def create_test_data():  # Optional. Used to test database functions before gui is ready.
   with Session(engine) as session:
       new_items = []
       new_items.append(Container(weight=1200, destination="Oslo"))
       new_items.append(Container(weight=700, destination="Helsinki"))
       new_items.append(Container(weight=1800, destination="Helsinki"))
       new_items.append(Container(weight=1000, destination="Helsinki"))
       session.add_all(new_items)
       session.commit()