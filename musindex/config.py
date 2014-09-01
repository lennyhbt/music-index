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

