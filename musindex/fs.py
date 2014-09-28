# -*- coding: utf-8 -*-
"""
    musicindex.fs
    ~~~~~~~~~~~~~~~~~~~

    This module scan dir and parse fileinfo.

    :copyright: (c) 2014 by Lenny.
    :license: LGPL, see LICENSE for more details.
"""

import os, stat
import mimetypes
from musindex import db

mimetypes.init()

class FileInfo(object):
    '''file info contaions file's path and mimetype info.'''
    # all allowed attributes
    __slots__ = ('uri', 'fullname', 'basedir', 'filename', 'suffix', 'mimetype')
    def __init__(self, fname):
        self.fullname = os.path.abspath(fname)
        if not os.path.isfile(self.fullname):
            # error
            pass
        self.basedir = os.path.dirname(self.fullname)
        self.filename = os.path.basename(self.fullname)
        self.uri = 'file://' + self.fullname
        self.suffix = os.path.splitext(self.fullname)[1]
        self.mimetype = mimetypes.guess_type(self.uri, strict=False)[0]


def scan_dirs(repo, opfunc):
    '''scan a dir path and do opfunc for every file in the dir.'''
    if not os.path.exists(repo):
        return
    new_m = os.stat(repo)[stat.ST_MTIME]
    last_m = 0
    from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
    repo = os.path.abspath(repo)
    dbs = db.SESSION()
    try:
        last_m = dbs.query(db.RepoInfo).filter(db.RepoInfo.path == repo).one().timestamp
    except NoResultFound: # add this repo to db
        new_repo = db.RepoInfo(path=repo, timestamp=new_m)
        dbs.add(new_repo)
        dbs.commit()
    dbs.close()
    if last_m >= new_m:
        return
    for root, dirs, files in os.walk(repo):
        for f in files:
            new_m = os.stat(os.path.join(root,f))[stat.ST_MTIME]
            if last_m >= new_m:
                continue
            opfunc(FileInfo(os.path.join(root,f)))

if __name__ == '__main__':
    def print_op(f):
        print(f.fullname)
        print('\turi:{0}'.format(f.uri))
        print('\tbasedir:{0}'.format(f.basedir))
        print('\tfilename:{0}'.format(f.filename))
        print('\tsuffix:{0}'.format(f.suffix))
        print('\tmimetype:{0}'.format(f.mimetype))
    import os
    scan_dirs(os.getcwd(), print_op)
