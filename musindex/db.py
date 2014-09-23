# -*- coding: utf-8 -*-
"""
    musicindex.db
    ~~~~~~~~~~~~~~~~~~~

    This module store all music info into db.

    :copyright: (c) 2014 by Lenny.
    :license: LGPL, see LICENSE for more details.
"""

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os

from musindex import config

DB_CONN = config.get_config('db_conn')

if DB_CONN is None or DB_CONN == '':
    DB_CONN = 'sqlite:///:memory:'
ENGINE = create_engine(DB_CONN, echo=False)
SESSION = sessionmaker(bind=ENGINE)
DBASE = declarative_base()
DBASE.metadata.create_all(ENGINE)

class RepoInfo(DBASE):
    __tablename__ = 'repoinfo'

    id = Column(Integer, primary_key=True)
    path = Column(String)
    timestamp = Column(Integer)

class MusicFile(DBASE):
    __tablename__ = 'musicfile'

    id = Column(Integer, primary_key=True)
    filetype = Column(String)
    uri = Column(String)
    path = Column(String)
    basedir = Column(String)
    filename = Column(String)
    suffix = Column(String)
    mimetype = Column(String)

    def __repr__(self):
        return "<file(uri='{0}', path='{1}')>".format(self.uri, self.path)

class Artist(DBASE):
    __tablename__ = 'artist'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return '<Artist(name={0})>'.format(self.name)

class Album(DBASE):
    __tablename__ = 'album'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return '<Album(name={0})>'.format(self.name)

class Song(DBASE):
    __tablename__ = 'song'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    genre = Column(String)
    year = Column(String)

    def __repr__(self):
        return '<Song(name={0})>'.format(self.name)

class MsuicRefer(DBASE):
    '''relation between file,song,artist and album'''
    __tablename__ = 'relate'

    id = Column(Integer, primary_key=True)
    fileid = Column(Integer)
    songid = Column(Integer)
    artistid = Column(Integer)
    albumid = Column(Integer)

    def __repr__(self):
        return '<MusicRefer(fileid={0},songid={1},artistid={2},albumid={3})>'.format(
            self.fileid, self.songid, self.artistid, self.artistid)

class TagRefer(DBASE):
    '''relation between a music object and a tag.'''
    __tablename__ = 'tagrel'

    id = Column(Integer, primary_key=True)
    cid = Column(Integer)
    ctype = Column(Integer)
    tag = Column(String)

    def __repr__(self):
        cate = "Unknow"
        if self.ctype == 1:
            cate = "song"
        elif self.ctype == 2:
            cate = "artist"
        elif self.ctype == 3:
            cate = "album"

        return '<TagRefer({0}:{1} tag {2})>'.format(cate, self.cid, self.tag)

if __name__ == '__main__':
    import os
    import fs
    DBASE.metadata.create_all(ENGINE)
    s = SESSION()

    def save_db(f):
        finfo = MusicFile(uri=f.uri, path=f.fullname, basedir=f.basedir,
                         filename=f.filename, suffix=f.suffix, mimetype=f.mimetype)
        s.add(finfo)
    fs.scan_dirs(os.getcwd(), save_db)
    s.commit()

    print('files:\n')
    for f in s.query(MusicFile).order_by(MusicFile.uri):
        print(f.uri)

