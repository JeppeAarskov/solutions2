from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import create_engine, select


Database = 'sqlite:///data/eksamen_database.db'
Base = declarative_base()


def set_sqlite_pragma(dbapi_connection, connection_record):
   cursor = dbapi_connection.cursor()
   cursor.execute("PRAGMA foreign_keys=ON")
   cursor.close()


def select_all(classparam):  # return a list of all records in classparams table
    with Session(engine) as session:
        records = session.scalars(select(classparam))
        result = []
        for record in records:
            result.append(record)
    return result


# region common functions
def empty_treeview(tree):  # Clear treeview table
   tree.delete(*tree.get_children())


def create_record(record): # https://docs.sqlalchemy.org/en/14/tutorial/orm_data_manipulation.html#orm-enabled-update-statements
    with Session(engine) as session:
        record.id = None
        session.add(record)
        session.commit() # makes changes permanent in database


def get_record(classparam, record_id):  # return the record in classparams table with a certain id   https://docs.sqlalchemy.org/en/14/tutorial/data_select.html
    with Session(engine) as session:
        # in the background this creates the sql query "select * from persons where id=record_id" when called with classparam=Person
        record = session.scalars(select(classparam).where(classparam.id == record_id)).first()
    return record


engine = create_engine(Database, echo=False, future=True)
Base.metadata.create_all(engine)