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
    '''initialize music repository'''
    db.DBASE.metadata.create_all(db.ENGINE)

    def save_db(finfo):
        '''save file info into database'''
        if finfo.mimetype is not None and finfo.mimetype.find('audio') != -1:
            dbs = db.SESSION()
            finfo = db.MusicFile(path=finfo.fullname, filename=finfo.filename,
                                 mimetype=finfo.mimetype)
            dbs.add(finfo)

            # analysis metadata
            meta = metadata.MusicFile(fs.FileInfo(finfo.path))
            song = dbs.query(db.Song).filter(db.Song.name == meta.title)
            if song.count() == 0:
                song = db.Song(name=meta.title, genre=meta.genre, year=meta.year)
                dbs.add(song)
            art = dbs.query(db.Artist).filter(db.Artist.name == meta.artist)
            if art.count() == 0:
                art = db.Artist(name=meta.artist)
                dbs.add(art)
            album = dbs.query(db.Album).filter(db.Album.name == meta.album)
            if album.count() == 0:
                album = db.Album(name=meta.album)
                dbs.add(album)

            art = dbs.query(db.Artist).filter(db.Artist.name == meta.artist)
            artid = art[0].id
            album = dbs.query(db.Album).filter(db.Album.name == meta.album)
            albumid = album[0].id
            song = dbs.query(db.Song).filter(db.Song.name == meta.title)
            songid = song[0].id
            music_ref = db.MusicRefer(fileid=finfo.id, songid=songid,
                                    artistid=artid, albumid=albumid)
            dbs.add(music_ref)
            dbs.commit()
            dbs.close()

    config.init()
    # remove old invalid files
    dbs = db.SESSION()
    for finfo in dbs.query(db.MusicFile).order_by(db.MusicFile.path):
        meta = metadata.MusicFile(fs.FileInfo(finfo.path))

        if not os.path.isfile(finfo.path):
            # delete invalid files
            song = dbs.query(db.Song).filter(db.Song.name == meta.title)
            if song.count() != 0:
                dbs.query(db.MusicRefer).filter(db.MusicRefer.fileid ==
                                                finfo.id).delete()
                dbs.query(db.TagRefer).filter(db.TagRefer.ctype == 1).filter(
                    db.TagRefer.cid == song[0].id).delete()
            dbs.delete(finfo)
            continue
    dbs.close()

    # scan new files
    repos = config.get_config('dirs')
    for repo in repos.split(':'):
        if repo.strip() != '':
            repo = os.path.abspath(os.path.expanduser(repo))
            fs.scan_dirs(repo, save_db)

if __name__ == '__main__':
    config.get_config('db_conn')
