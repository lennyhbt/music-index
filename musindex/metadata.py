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

'''
ape:
    Title，Artist, Album, Year, Catalog
flac:
    title, artist, album, data, genre
mp3:
    Title, Artist, Album, Year, Genre
0="Blues";                       1="ClassicRock";                       2="Country";
3="Dance";                       4="Disco";                             5="Funk";
6="Grunge";                      7="Hip-Hop";                           8="Jazz";
9="Metal";                       10="NewAge";                          11="Oldies";
12="Other";                      13="Pop";                             14="R&B";
15="Rap";                        16="Reggae";                          17="Rock";
18="Techno";                     19="Industrial";                      20="Alternative";
21="Ska";                        22="DeathMetal";                      23="Pranks";
24="Soundtrack";                 25="Euro-Techno";                     26="Ambient";
27="Trip-Hop";                   28="Vocal";                           29="Jazz+Funk";
30="Fusion";                     31="Trance";                          32="Classical";
33="Instrumental";               34="Acid";                            35="House";
36="Game";                       37="SoundClip";                       38="Gospel";
39="Noise";                      40="AlternRock";                      41="Bass";
42="Soul";                       43="Punk";                            44="Space";
45="Meditative";                 46="InstrumentalPop";                 47="InstrumentalRock";
48="Ethnic";                     49="Gothic";                          50="Darkwave";
51="Techno-Industrial";          52="Electronic";                      53="Pop-Folk";
54="Eurodance";                  55="Dream";                           56="SouthernRock";
57="Comedy";                     58="Cult";                            59="Gangsta";
60="Top40";                      61="ChristianRap";                    62="Pop/Funk";
63="Jungle";                     64="NativeAmerican";                  65="Cabaret";
66="NewWave";                    67="Psychadelic";                     68="Rave";
69="Showtunes";                  70="Trailer";                         71="Lo-Fi";
72="Tribal";                     73="AcidPunk";                        74="AcidJazz";
75="Polka";                      76="Retro";                           77="Musical";
78="Rock&Roll";                  79="HardRock";                        80="Folk";
81="Folk-Rock";                  82="NationalFolk";                    83="Swing";
84="FastFusion";                 85="Bebob";                           86="Latin";
87="Revival";                    88="Celtic";                          89="Bluegrass";
90="Avantgarde";                 91="GothicRock";                      92="ProgessiveRock";
93="PsychedelicRock";            94="SymphonicRock";                   95="SlowRock";
96="BigBand";                    97="Chorus";                          98="EasyListening";
99="Acoustic";                   100="Humour";                         101="Speech";
102="Chanson";                   103="Opera";                          104="ChamberMusic";
105="Sonata";                    106="Symphony";                       107="BootyBass";
108="Primus";                    109="PornGroove";                     110="Satire";
111="SlowJam";                   112="Club";                           113="Tango";
114="Samba";                     115="Folklore";                       116="Ballad";
117="PowerBallad";               118="RhythmicSoul";                   119="Freestyle";
120="Duet";                      121="PunkRock";                       122="DrumSolo";
123="Acapella";                  124="Euro-House";                     125="DanceHall";
126="Goa";                       127="Drum&Bass";                      128="Club-House";
129="Hardcore";                  130="Terror";                         131="Indie";
132="BritPop";                   133="Negerpunk";                      134="PolskPunk";
135="Beat";                      136="ChristianGangstaRap";            137="HeavyMetal";
138="BlackMetal";                139="Crossover";                      140="ContemporaryChristian";
141="ChristianRock";             142="Merengue";                       143="Salsa";
144="TrashMetal";                145="Anime";                          146="JPop";
147="Synthpop";
'''

import mutagenx

metadata = mutagenx.File('/home/lenny/音乐/The_Band_Perry_If_I_Die_Young.flac')

class MusicFile(object):
    def __init__(self, name):
        self.metadata = mutagenx.File(name)
        self.tags = self.metadata.tags

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

