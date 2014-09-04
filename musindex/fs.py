# -*- coding: utf-8 -*-
"""
    musicindex.fs
    ~~~~~~~~~~~~~~~~~~~

    This module scan dir and parse fileinfo.

    :copyright: (c) 2014 by Lenny.
    :license: LGPL, see LICENSE for more details.
"""

import os
import mimetypes

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


def scan_dirs(path, opfunc):
    '''scan a dir path and do opfunc for every file in the dir.'''
    for root, dirs, files in os.walk(path):
        for f in files:
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
