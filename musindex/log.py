# -*- coding: utf-8 -*-
"""
    musicindex.log
    ~~~~~~~~~~~~~~~~~~~

    This module provide log function for music index.

    :copyright: (c) 2014 by Lenny.
    :license: LGPL, see LICENSE for more details.
"""

import logging

from musindex import config

def log_config():
    '''config log fuction'''
    level_dict = {
        "DEBUG":logging.DEBUG, "INFO":logging.INFO,
        "WARNING":logging.WARNING, "ERROR":logging.ERROR,
        "CRITICAL":logging.CRITICAL
    }

    logfile = config.get_config('logfile')
    if config.get_config('loglevel') not in level_dict:
        loglevel = level_dict['DEBUG']
    else:
        loglevel = level_dict[config.get_config('loglevel')]
    logging.basicConfig(filename=logfile, level=loglevel)

def log(msg, level='DEBUG'):
    '''log function for musindex'''
    if level == 'DEBUG':
        logging.debug(msg)
    elif level == 'INFO':
        logging.info(msg)
    elif level == 'WARNING':
        logging.warning(msg)
    elif level == 'ERROR':
        logging.error(msg)
    elif level == 'CRITICAL':
        logging.critical(msg)

log_config()
