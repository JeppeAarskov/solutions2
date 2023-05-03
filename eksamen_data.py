from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import create_engine, select
from sqlalchemy import Column, Integer, Date

Base = declarative_base()

# Every single class listed here
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

    @staticmethod
    def convert_from_tuple(tuple_):
        container = Hold(id=[0], erfaring=[1], størrelse=[2])
        container2 = Booking(id=[0], dato=[1], hold_id=[2])
        return container
        return container2


class Booking(Base):
    __tablename__ = "Booking"
    id = Column(Integer, primary_key=True)
    dato = Column(Date)
    hold_id = Column(Integer)
    bane_id = Column(Integer)

    def __repr__(self):
        return f"Booking({self.id=} {self.dato=} {self.hold_id=} {self.bane_id=})"

    @staticmethod
    def convert_from_tuple(tuple_):
        container = Hold(id=[0], erfaring=[1], størrelse=[2])
        container2 = Booking(id=[0], dato=[1], hold_id=[2])
        return container
        return container2


Database = 'sqlite:///data/eksamen_database.db'
engine = create_engine(Database, echo=False, future=True)
Base.metadata.create_all(engine)
