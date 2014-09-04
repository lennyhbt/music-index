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

import mutagenx

#metadata = mutagenx.File('/home/lenny/音乐/The_Band_Perry_If_I_Die_Young.flac')

class MusicFile(object):
    __slots__ = ('filetype', 'filename', 'title', 'artist', 'album', 'genre', 'year')


    genre = [
        "Blues",                     "ClassicRock",                    "Country",
        "Dance",                     "Disco",                          "Funk",
        "Grunge",                    "Hip-Hop",                        "Jazz",
        "Metal",                     "NewAge",                         "Oldies",
        "Other",                     "Pop",                            "R&B",
        "Rap",                       "Reggae",                         "Rock",
        "Techno",                    "Industrial",                     "Alternative",
        "Ska",                       "DeathMetal",                     "Pranks",
        "Soundtrack",                "Euro-Techno",                    "Ambient",
        "Trip-Hop",                  "Vocal",                          "Jazz+Funk",
        "Fusion",                    "Trance",                         "Classical",
        "Instrumental",              "Acid",                           "House",
        "Game",                      "SoundClip",                      "Gospel",
        "Noise",                     "AlternRock",                     "Bass",
        "Soul",                      "Punk",                           "Space",
        "Meditative",                "InstrumentalPop",                "InstrumentalRock",
        "Ethnic",                    "Gothic",                         "Darkwave",
        "Techno-Industrial",         "Electronic",                     "Pop-Folk",
        "Eurodance",                 "Dream",                          "SouthernRock",
        "Comedy",                    "Cult",                           "Gangsta",
        "Top40",                     "ChristianRap",                   "Pop/Funk",
        "Jungle",                    "NativeAmerican",                 "Cabaret",
        "NewWave",                   "Psychadelic",                    "Rave",
        "Showtunes",                 "Trailer",                        "Lo-Fi",
        "Tribal",                    "AcidPunk",                       "AcidJazz",
        "Polka",                     "Retro",                          "Musical",
        "Rock&Roll",                 "HardRock",                       "Folk",
        "Folk-Rock",                 "NationalFolk",                   "Swing",
        "FastFusion",                "Bebob",                          "Latin",
        "Revival",                   "Celtic",                         "Bluegrass",
        "Avantgarde",                "GothicRock",                     "ProgessiveRock",
        "PsychedelicRock",           "SymphonicRock",                  "SlowRock",
        "BigBand",                   "Chorus",                         "EasyListening",
        "Acoustic",                  "Humour",                         "Speech",
        "Chanson",                   "Opera",                          "ChamberMusic",
        "Sonata",                    "Symphony",                       "BootyBass",
        "Primus",                    "PornGroove",                     "Satire",
        "SlowJam",                   "Club",                           "Tango",
        "Samba",                     "Folklore",                       "Ballad",
        "PowerBallad",               "RhythmicSoul",                   "Freestyle",
        "Duet",                      "PunkRock",                       "DrumSolo",
        "Acapella",                  "Euro-House",                     "DanceHall",
        "Goa",                       "Drum&Bass",                      "Club-House",
        "Hardcore",                  "Terror",                         "Indie",
        "BritPop",                   "Negerpunk",                      "PolskPunk",
        "Beat",                      "ChristianGangstaRap",            "HeavyMetal",
        "BlackMetal",                "Crossover",                      "ContemporaryChristian",
        "ChristianRock",             "Merengue",                       "Salsa",
        "TrashMetal",                "Anime",                          "JPop",
        "Synthpop",
    ]

    def __init__(self, name):
        self.metadata = mutagenx.File(name)

        if 'mp3' in self.metadata.mime[0]:
            self.filetype = 1
            self.filename = name
        elif 'wma' in self.metadata.mime[0]:
            pass
        elif 'flac' in self.metadata.mime[0]:
            pass
        elif 'ape' in self.metadata.mime[0]:
            pass
        elif 'ogg' in self.metadata.mime[0]:
            pass
        elif 'asf' in self.metadata.mime[0]:
            pass
        elif 'mp4' in self.metadata.mime[0]:
            pass

    apetag = {'title':'Title', 'artist':'Artist', 'album':'Album', 'year':'Year', 'genre':'Catalog'}
    flactag = {'title':'title', 'artist':'artist', 'album':'album', 'year':'year', 'genre':'genre'}
    mp3tag = {'title':'Title', 'artist':'Artist', 'album':'Album', 'year':'Year', 'genre':'Genre'}
        self.title = self.metadata.get('title', 'Unknown')
        self.artist = self.metadata.get('artist', 'Unknown')
        self.album = self.metadata.get('album', 'Unkonwn')
        self.genre = self.metadata.get('genre')
        self.year = self.metadata.get('year')



