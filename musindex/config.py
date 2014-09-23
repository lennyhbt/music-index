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

CONF_FILE = '~/.musindex/musindex.conf'

def get_config(opt, boolen=0):
    '''get a config opt according to config[section][opt] and value type.'''
    section = 'musindex repo'
    config = configparser.ConfigParser()
    config.read(CONF_FILE)
    ret = None
    if section not in config.sections():
        ret = None
    elif boolen != 0:
        ret = config[section].getboolean(opt, False)
    else:
        ret = config[section].get(opt, '')
    return ret

def set_config(opt, val):
    '''set a config opt according to config[section][opt] and value.'''
    section = 'musindex repo'
    config = configparser.ConfigParser()
    config.read(CONF_FILE)
    if section not in config:
        config[section] = {}
    config[section][opt] = val

    with open(os.path.join(os.getcwd(), 'musindex.conf'), 'w') as conf:
        config.write(conf)

def set_defconfig():
    set_config('dirs', '~/music:')
    #set_config('db_conn', 'sqlite:///~/.musindex/musicrepo.db')
    set_config('db_conn', 'sqlite:///:memory:')
    set_config('loglevel', 'DEBUG')
    set_config('logfile', '~/.musindex/musindex.log')

def init():
    if not os.path.isfile(CONF_FILE):
        set_defconfig()
