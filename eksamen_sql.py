from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import create_engine, select
from sqlalchemy import Column, Integer, Date

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

class Hold(Base):
    __tablename__ = "Hold"
    id = Column(Integer, primary_key=True)
    erfaring = Column(Integer)
    størrelse = Column(Integer)

    def __repr__(self):
        return f"Hold({self.id=} {self.erfaring=} {self.størrelse=})"


class Bane(Base):
    __tablename__ = "Bane"
    id = Column(Integer, primary_key=True)
    kapacitet = Column(Integer)
    sværhedsgrad = Column(Integer)

    def __repr__(self):
        return f"Bane({self.id=} {self.kapacitet=} {self.sværhedsgrad=})"


class Booking(Base):
    __tablename__ = "Booking"
    id = Column(Integer, primary_key=True)
    dato = Column(Date)
    hold_id = Column(Integer)
    bane_id = Column(Integer)

    def __repr__(self):
        return f"Booking({self.id=} {self.dato=} {self.hold_id=} {self.bane_id=})"


def get_record(classparam, record_id):  # return the record in classparams table with a certain id   https://docs.sqlalchemy.org/en/14/tutorial/data_select.html
    with Session(engine) as session:
        # in the background this creates the sql query "select * from persons where id=record_id" when called with classparam=Person
        record = session.scalars(select(classparam).where(classparam.id == record_id)).first()
    return record


engine = create_engine(Database, echo=False, future=True)
Base.metadata.create_all(engine)