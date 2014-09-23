# -*- coding: utf-8 -*-
"""
    musicindex.app
    ~~~~~~~~~~~~~~~~~~~

    musindex app for run.

    :copyright: (c) 2014 by Lenny.
    :license: LGPL, see LICENSE for more details.
"""

import os,stat
from musindex import metadata, fs, cue, db, config, log

#def new_music(f):
#    dbs = db.SESSION()
#    finfo = db.MusicFile(uri=f.uri, path=f.fullname, basedir=f.basedir,
#                        filename=f.filename, suffix=f.suffix, mimetype=f.mimetype)
#    dbs.add(finfo)
#    dbs.commit()
#    dbs.close()

def init():
    # initialize music repository
    db.DBASE.metadata.create_all(db.ENGINE)

    def save_db(f):
        dbs = db.SESSION()
        finfo = db.MusicFile(uri=f.uri, path=f.fullname, basedir=f.basedir,
                         filename=f.filename, suffix=f.suffix, mimetype=f.mimetype)
        dbs.add(finfo)
        dbs.commit()
        dbs.close()

    config.init()
    # scan new files
    repos = config.get_config('dirs')
    for repo in repos.split(':'):
        fs.scan_dirs(repo, save_db)
    # analysis metadata
    dbs = db.SESSION()
    for f in dbs.query(db.MusicFile).order_by(db.MusicFile.uri):
        m = metadata.MusicFile(fs.FileInfo(f.path))

        art = dbs.query(db.Artist).filter(db.Artist.name == m.artist)
        if len(art) == 0:
            art = db.Artist(name=m.artist)
            dbs.add(art)
        album = dbs.query(db.Album).filter(db.Album.name == m.artist)
        if len(album) == 0:
            album = db.Album(name=m.album)
            dbs.add(album)

        song = dbs.query(db.Song).filter(db.Song.name == m.title)
        if len(song) == 0:
            song = db.Album(name=m.album, genre=m.genre, year=m.year)
            dbs.add(song)
        dbs.commit()

        music_ref  = db.MusicRefer(fileid=f.id, songid=, artistid=,albumid=)
        dbs.add(music_ref)
        dbs.commit()
    # delete invalid files
    dbs.close()

if __name__ == '__main__':
    config.get_config('db_conn')
