# -*- coding: utf-8 -*-
"""
    musicindex.config
    ~~~~~~~~~~~~~~~~~~~

    This module offer config interface for music index.

    :copyright: (c) 2014 by Lenny.
    :license: LGPL, see LICENSE for more details.
"""

import os
import configparser

def get_config(section, item, typ):
    '''get a config item according to config[section][item] and value type.'''
    config = configparser.ConfigParser()
    config.read('musindex.conf')
    ret = None
    if typ == 'int':
        ret = config[section].getInt(item)
    elif typ == 'float':
        ret = config[section].getfloat(item)
    elif typ == 'bool':
        ret = config[section].getboolean(item)
    else:
        ret = config[section].get(item)
    return ret

def set_config(section, item, val):
    '''set a config item according to config[section][item] and value.'''
    config = configparser.ConfigParser()
    config.read('musindex.conf')
    config[section][item] = val

    with open(os.path.join(os.getcwd(), 'musindex.conf'), 'w') as conf:
        config.write(conf)

def set_defconfig():
    pass

