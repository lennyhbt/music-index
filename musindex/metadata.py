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

USE_TAGLIB = True
try:
    import taglib
except ImportError:
    USE_TAGLIB = False
    import mutagenx

class MusicFile(object):

    """" MusicFile contains audio metadata and file info. """

    __slots__ = ('filetype', 'filename', 'metadata',
                 'title', 'artist', 'album', 'genre', 'year')

    __genre_code = {
        0: "Blues", 1: "Classic Rock", 2: "Country", 3: "Dance",
        4: "Disco", 5: "Funk", 6: "Grunge", 7: "Hip-Hop", 8: "Jazz",
        9: "Metal", 10: "New Age", 11: "Oldies", 12: "Other", 13: "Pop",
        14: "R&B", 15: "Rap", 16: "Reggae", 17: "Rock", 18: "Techno",
        19: "Industrial", 20: "Alternative", 21: "Ska", 22: "Death Metal",
        23: "Pranks", 24: "Soundtrack", 25: "Euro-Techno", 26: "Ambient",
        27: "Trip-Hop", 28: "Vocal", 29: "Jazz+Funk", 30: "Fusion",
        31: "Trance", 32: "Classical", 33: "Instrumental", 34: "Acid",
        35: "House", 36: "Game", 37: "Sound Clip", 38: "Gospel",
        39: "Noise", 40: "AlternRock", 41: "Bass", 42: "Soul", 43: "Punk",
        44: "Space", 45: "Meditative", 46: "Instrumental Pop",
        47: "Instrumental Rock", 48: "Ethnic", 49: "Gothic", 50: "Darkwave",
        51: "Techno-Industrial", 52: "Electronic", 53: "Pop-Folk",
        54: "Eurodance", 55: "Dream", 56: "Southern Rock", 57: "Comedy",
        58: "Cult", 59: "Gangsta Rap", 60: "Top 40", 61: "Christian Rap",
        62: "Pop / Funk", 63: "Jungle", 64: "Native American", 65: "Cabaret",
        66: "New Wave", 67: "Psychedelic", 68: "Rave", 69: "Showtunes",
        70: "Trailer", 71: "Lo-Fi", 72: "Tribal", 73: "Acid Punk",
        74: "Acid Jazz", 75: "Polka", 76: "Retro", 77: "Musical",
        78: "Rock & Roll", 79: "Hard Rock", 80: "Folk", 81: "Folk-Rock",
        82: "National Folk", 83: "Swing", 84: "Fast  Fusion", 85: "Bebob",
        86: "Latin", 87: "Revival", 88: "Celtic", 89: "Bluegrass",
        90: "Avantgarde", 91: "Gothic Rock", 92: "Progressive Rock",
        93: "Psychedelic Rock", 94: "Symphonic Rock", 95: "Slow Rock",
        96: "Big Band", 97: "Chorus", 98: "Easy Listening", 99: "Acoustic",
        100: "Humour", 101: "Speech", 102: "Chanson", 103: "Opera",
        104: "Chamber Music", 105: "Sonata", 106: "Symphony",
        107: "Booty Bass", 108: "Primus", 109: "Porn Groove", 110: "Satire",
        111: "Slow Jam", 112: "Club", 113: "Tango", 114: "Samba",
        115: "Folklore", 116: "Ballad", 117: "Power Ballad",
        118: "Rhythmic Soul", 119: "Freestyle", 120: "Duet", 121: "Punk Rock",
        122: "Drum Solo", 123: "A Cappella", 124: "Euro-House",
        125: "Dance Hall", 126: "Goa", 127: "Drum & Bass", 128: "Club-House",
        129: "Hardcore", 130: "Terror", 131: "Indie", 132: "BritPop",
        133: "Negerpunk", 134: "Polsk Punk", 135: "Beat",
        136: "Christian Gangsta Rap", 137: "Heavy Metal", 138: "Black Metal",
        139: "Crossover", 140: "Contemporary Christian", 141: "Christian Rock",
        142: "Merengue", 143: "Salsa", 144: "Thrash Metal", 145: "Anime",
        146: "JPop", 147: "Synthpop", 148: "Rock/Pop",
    }

    def_title = 'FreeMusic'
    def_artist = 'FreeArtist'
    def_album = 'FreeAlbum'
    def_genre = 'FreeGenre'
    # the first record of the world is in 1888
    def_year = '1887'

    def __init__(self, fileinfo):
        self.__tagfile = None
        self.__title = None
        self.__artist = None
        self.__album = None
        self.__genre = None
        self.__year = None
        self.mimetype = fileinfo.mimetype
        self.filename = fileinfo.fullname
        if 'mp3' in self.mimetype:
            self.filetype = 1
        elif 'wma' in self.mimetype:
            self.filetype = 2
        elif 'flac' in self.mimetype:
            self.filetype = 3
        elif 'ape' in self.mimetype:
            self.filetype = 4
        elif 'ogg' in self.mimetype:
            self.filetype = 5
        elif 'asf' in self.mimetype:
            self.filetype = 6
        elif 'mp4' in self.mimetype:
            self.filetype = 7

        get_metadata()

    def get_metadata(self):
        '''get all metadata from the music file.'''
        if USE_TAGLIB:
            self.__tagfile = taglib.File(self.filename)
            tags = self.__tagfile.tags
            self.__title = tags.get('TITLE', self.def_title)
            self.__artist = tags.get('ARTIST', self.def_artist)
            self.__album = tags.get('ALBUM', self.def_album)
            self.__genre = tags.get('GENRE', self.def_genre)
            self.__year = tags.get('DATE', self.def_year)
        else:
            self.__tagfile = mutagenx.File(self.filename).tags
            tags = self.__tagfile.tags
            self.__title = tags.get('TITLE')
            self.__artist = tags.get('ARTIST')
            self.__album = tags.get('ALBUM')
            self.__genre = tags.get('GENRE')
            self.__year = tags.get('DATE')

            if self.__title is None:
                self.__title = tags.get('TIT2', self.def_title)
            if self.__artist is None:
                self.__artist = tags.get('TPE1', self.def_artist)
            if self.__album is None:
                self.__album = tags.get('TALB', self.def_album)
            if self.__genre is None:
                self.__genre = tags.get('TCON', self.def_genre)
            if self.__year is None:
                self.__year = tags.get('TYER', self.def_year)

        if self.__genre.isdigit():
            self.__genre = self.__genre_code[int(self.__genre)]

    def save_to_file(self):
        '''set tags to the file'''
        # TODO:implement it
        pass

    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title):
        self.__title = title;
        self.save_to_file()

    @property
    def artist(self):
        return self.__artist
    @artist.setter
    def artist(self, artist):
        self.__artist = artist;
        self.save_to_file()

    @property
    def album(self):
        return self.__album
    @album.setter
    def album(self, album):
        self.__album = album;
        self.save_to_file()

    @property
    def genre(self):
        return self.__genre
    @genre.setter
    def genre(self, genre):
        self.__genre = genre;
        self.save_to_file()

    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self, year):
        self.__year = year
        self.save_to_file()

