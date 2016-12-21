import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

class Comentarios(Base):
    __tablename__ = 'comentario'

    id = Column(Integer, primary_key=True)
    content = Column(String(250), nullable=False)
    creacion = Colum()
    user_id = Colum(Integer, ForeignKey('user.id')) 


engine = create_engine('sqlite:///comentario.db')


Base.metadata.create_all(engine)