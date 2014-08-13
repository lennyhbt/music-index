# -*- coding: utf-8 -*-
"""
    musicindex.metadata
    ~~~~~~~~~~~~~~~~~~~

    This module provides functios for getting musci file's metadata.

    we are insrested in these metadatas:
        * filename
        * title
        * artist
        * album
        * genre
        * year

    :copyright: (c) 2014 by Lenny.
    :license: LGPL, see LICENSE for more details.
"""

import mutagen

metadata = mutagen.File('/home/lenny/音乐/The_Band_Perry_If_I_Die_Young.flac')

class MusicFile(object):
    def __init__(self, name):
        self.metadata = mutagen.File(name)

    def get_filetype(self):
        pass

    @property
    def filename(self):
        return self._fname

    @filename.setter
    def filename(self, val):
        self._fname = val

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, val):
        self._title = val

    @property
    def artist(self):
        return self._artist

    @artist.setter
    def artist(self, val):
        self._artist = val

    @property
    def album(self):
        return self._album

    @album.setter
    def album(self, val):
        self._album = val

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, val):
        self._genre = val

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, val):
        self._year = val

