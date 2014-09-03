from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#engine = create_engine('sqlite:///:memory:', echo=False)
import os
engine = create_engine('sqlite:///{0}/musindex.db'.format(os.getcwd()), echo=False)
Session = sessionmaker(bind=engine)

DBase = declarative_base()
DBase.metadata.create_all(engine)

class FileList(DBase):
    __tablename__ = 'file'
    id = Column(Integer, primary_key=True)
    uri = Column(String)
    path = Column(String)
    basedir = Column(String)
    filename = Column(String)
    suffix = Column(String)
    mimetype = Column(String)

    def __repr__(self):
        return "<file(uri='{0}', path='{1}')>".format(self.uri, self.path)

class Artist(DBase):
    __tablename__ = 'artist'

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Album(DBase):
    __tablename__ = 'album'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    artist = Column(String)

    def __repr__(self):
        return '<Album(name={0})>'.format(self.name)

class Song(DBase):
    __tablename__ = 'song'

    id = Column(Integer, primary_key=True)
    fname = Column(String)
    name = Column(String)
    artist = Column(Integer)
    album = Column(Integer)

class Refer(DBase):
    __tablename__ = 'relate'

    id = Column(Integer, primary_key=True)
    fileid = Column(Integer)
    songid = Column(Integer)
    artistid = Column(Integer)
    albumid = Column(Integer)

class TagRefer(DBase):
    __tablename__ = 'tagrel'

    id = Column(Integer, primary_key=True)
    cid = Column(Integer)
    ctype = Column(Integer)
    tag = Column(String)

if __name__ == '__main__':
    import os
    import fs
    DBase.metadata.create_all(engine)
    s = Session()

    def save_db(f):
        finfo = FileList(uri=f.uri, path=f.fullname, basedir=f.basedir, filename=f.filename, suffix=f.suffix, mimetype=f.mimetype)
        s.add(finfo)
    fs.scan_dirs(os.getcwd(), save_db)
    s.commit()

    print('files:\n')
    for f in s.query(FileList).order_by(FileList.uri):
        print(f.uri)

