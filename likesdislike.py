import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

class LikesDislikes(Base):
    __tablename__ = 'likes_dislikes'

    id = Column(Integer, primary_key=True)
    foro_id = Column(Integer, ForeignKey('fotos.id'))
    like = Colum(Integer,nullable=False)
    dislike = Colum(Integer,nullable=False)
    creacion = Colum()
    user_id = Colum(Integer, ForeignKey('user.id')) 

engine = create_engine('sqlite:///likes_dislikes.db')


Base.metadata.create_all(engine)