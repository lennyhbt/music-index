from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory:', echo=False)
Session = sessionmaker(bind=engine)

DBase = declarative_base()
DBase.metadata.create_all(engine)

class Album(DBase):
    __tablename__ = 'album'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return '<Album(name={0})>'.format(self.name)

#a = Album()
#a.id = 1
#session.add(a)
