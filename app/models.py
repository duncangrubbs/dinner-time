from sqlalchemy import Column, Integer, String, PickleType

from .database import Base


class Meal(Base):
    __tablename__ = "meals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    season = Column(String)
    category = Column(String)
    ingredients = Column(PickleType)
    url = Column(String)
    last_suggested = Column(Integer)
