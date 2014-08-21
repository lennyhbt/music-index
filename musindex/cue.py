# -*- coding: utf-8 -*-
"""
    musicindex.cue
    ~~~~~~~~~~~~~~~~~~~

    This module provides functios for parsing album cue info.

    :copyright: (c) 2014 by Lenny.
    :license: LGPL, see LICENSE for more details.
"""

import os
import chardet

class CUEINFO(object):
    # album_info album global info, eg: album name, audio file name, artist
    album_info = {}
    # track_info each track info
    track_info = []
    def __init__(self, cue_filename):
        self.get_info(cue_filename)

    def get_info(self, filename):
        """
        Extracts Tags from the CUE Sheet
        """
        if os.path.getsize(filename) > 1024 * 1024:
            return

        self.album_info['cuefile'] = filename
        self.album_info['basedir'] = os.path.dirname(filename)

        file_enc = 'UTF-8'
        with open(filename, 'rb') as fp:
            buf = fp.read()
            enc = chardet.detect(buf)
            file_enc = enc['encoding']
        with open(filename, 'r', encoding=file_enc) as fp:
            lines = fp.readlines()

        i = -1
        for line in lines: # General info
            if line.startswith("FILE"):
                f = line.split("\"")[1]
                if not f.startswith("/"):
                    self.album_info['audio_filename'] = self.album_info['basedir'] + "/" + line.split("\"")[1]
            elif line.startswith("PERFORMER") and i == -1:
                self.album_info['artist'] = line.split("\"")[1]
            elif line.startswith("TITLE") and i == -1:
                self.album_info['name'] = line.split("\"")[1]
            elif line.strip().startswith("TRACK"): # Individual track info
                i += 1
                self.track_info.append( {} )
            elif line.strip().startswith("FILE") and i != -1:
                self.track_info[i]["audio_filename"] = line.split("\"")[1]
            elif line.strip().startswith("TITLE") and i != -1:
                self.track_info[i]["title"] = line.split("\"")[1]
            elif line.strip().startswith("PERFORMER") and i != -1:
                self.track_info[i]["artist"] = line.split("\"")[1]
            elif line.strip().startswith("INDEX 01") and i != -1:
                self.track_info[i]["index"] = line.split(" ")[-1].strip()

if __name__ == '__main__':
    import sys
    i = 1
    while i < len(sys.argv):
        cue = CUEINFO(sys.argv[i])
        print("album dir:{0}".format(cue.album_info.get('basedir')))
        print("album cuefile:{0}".format(cue.album_info.get('cuefile')))
        print("album audiofile:{0}".format(cue.album_info.get('audio_filename')))
        print("album name :{0}".format(cue.album_info.get('name')))
        print("album artist :{0}".format(cue.album_info.get('artist')))
        print("===>album trackinfo")
        #print("cue file[{0}] name:{1}".format(i, cue.cue_filename))
        j = 0
        while j < len(cue.track_info):
            print("\ttrack{0}: {1}".format(j, cue.track_info[j]))
            j += 1
        i += 1

