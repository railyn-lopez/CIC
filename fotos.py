import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

class Fotos(Base):
    __tablename__ = 'fotos'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    tag = Colum(String(400), nullable=False)
    creacion = Colum()
    user_id = Colum(Integer, ForeignKey('user.id')) 



engine = create_engine('sqlite:///fotos.db')


Base.metadata.create_all(engine)