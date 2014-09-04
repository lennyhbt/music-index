# -*- coding: utf-8 -*-
"""
    musicindex.config
    ~~~~~~~~~~~~~~~~~~~

    This module offer config interface for music index.

    :copyright: (c) 2014 by Lenny.
    :license: LGPL, see LICENSE for more details.
"""

import configparser

config = configparser.ConfigParser()
config['Default'] = {'test':123,'test2':'456'}
config['fs'] = {'dir':'~/music'}

import os
with open(os.path.join(os.getcwd(), 'musindex.conf'), 'w') as f:
    config.write(f)

config.read('musindex.conf')
#config['bitbucket.org'].getboolean('ForwardX11')
#config.sections()

