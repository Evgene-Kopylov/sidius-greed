from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.sql.schema import Table
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.sqltypes import DATE


@as_declarative()
class Base:
    id: Any
    __name__: str

    # to generate tablename from classname
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class Player(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String, unique=True)
    gold = Column(Integer, default=100)


class Hero(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    pathos = Column(Integer, default=0)
    force = Column(Integer, default=0)
    player = relationship("Player", backref="player_heroes")


class Item(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    value = Column(Integer)
    mod = Column(String)
    hero = relationship("Hero", backref="hero_items")
