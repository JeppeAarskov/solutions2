from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine, select


Database = 'sqlite:///data/eksamen_database.db'
Base = declarative_base()


def set_sqlite_pragma(dbapi_connection, connection_record):
   cursor = dbapi_connection.cursor()
   cursor.execute("PRAGMA foreign_keys=ON")
   cursor.close()


class Hold(Base):
    __tablename__ = "Hold"
    id = Column(Integer, primary_key=True)
    erfaring = Column(String)
    størrelse = Column(Integer)

    def __repr__(self):
        return f"Hold({self.id=} {self.erfaring=} {self.størrelse=})"


class Bane(Base):
    __tablename__ = "Bane"
    id = Column(Integer, primary_key=True)
    kapacitet = Column(String)
    sværhedsgrad = Column(Integer)

    def __repr__(self):
        return f"Bane({self.id=} {self.kapacitet=} {self.sværhedsgrad=})"


class Booking(Base):
    __tablename__ = "Booking"
    id = Column(Integer, primary_key=True)
    dato = Column(String)
    hold_id = Column(Integer)
    bane_id = Column(Integer)

    def __repr__(self):
        return f"Booking({self.id=} {self.dato=} {self.hold_id=} {self.bane_id=})"


def create_test_data():
    new_items = []
    new_items.append(Hold(id="1042", erfaring="27", størrelse=10))
    new_items.append(Hold(id="5975", erfaring="55", størrelse=5))
    new_items.append(Hold(id="2233", erfaring="35", størrelse=17))
    new_items.append(Bane(id="5490", kapacitet="65m2", sværhedsgrad="Let"))
    new_items.append(Bane(id="2349", kapacitet="22m2", sværhedsgrad="Meget svær"))
    new_items.append(Bane(id="1515", kapacitet="69m2", sværhedsgrad="Normal"))
    new_items.append(Booking(id="0093", dato="3/6/23", hold_id="875", bane_id="0912"))
    new_items.append(Booking(id="7827", dato="25/5/23", hold_id="332", bane_id="7395"))
    new_items.append(Booking(id="9427", dato="7/5/23", hold_id="593", bane_id="0204"))
    new_items.append(Booking(id="9421", dato="1/8/23", hold_id="223", bane_id="4491"))
    with Session(engine) as session:
        session.add_all(new_items)
        session.commit()


def select_all(classparam):  # return a list of all records in classparams table
    with Session(engine) as session:
        records = session.scalars(select(classparam))
        result = []
        for record in records:
            result.append(record)
    return result


def get_record(classparam, record_id):  # return the record in classparams table with a certain id   https://docs.sqlalchemy.org/en/14/tutorial/data_select.html
    with Session(engine) as session:
        # in the background this creates the sql query "select * from persons where id=record_id" when called with classparam=Person
        record = session.scalars(select(classparam).where(classparam.id == record_id)).first()
    return record


engine = create_engine(Database, echo=False, future=True)
Base.metadata.create_all(engine)

create_test_data()
print(get_record(Hold, 1))