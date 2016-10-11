'''
Utilties to read config.yaml.
'''
import os

import yaml


def read_config():
    '''Load yaml config'''

    with open(os.path.join(os.path.dirname(__file__), 'config.yaml'), 'r') as config_file:
        return yaml.load(config_file)

CONFIG = read_config()
