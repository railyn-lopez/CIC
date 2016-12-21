import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    contraseña = Column(String(250), nullable=False)
    correo = Column(String(250), nullable=False)
    fecha_nacimiento = Column(String(250), nullable=False)

engine = create_engine('sqlite:///user.db')


Base.metadata.create_all(engine)