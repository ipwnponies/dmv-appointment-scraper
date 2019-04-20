'''
Utilties to read config.yaml.
'''
from pathlib import Path

from strictyaml import load
from strictyaml import Map
from strictyaml import Str
from strictyaml import UniqueSeq
from strictyaml import Url

CONFIG_SCHEMA = Map({
    'mail': Map({
        'recipients': UniqueSeq(Str()),
        'sender': Str(),
        'subject': Str(),
        'password': Str(),
    }),
    'dmv': Map({
        'welcome_url': Url(),
        'user': Map({
            'first_name': Str(),
            'last_name': Str(),
            'area_code': Str(),
            'phone_prefix': Str(),
            'phone_suffix': Str(),
        }),
        'office': Str(),
        'task': Str(),
    }),
})


def read_config():
    '''Load yaml config'''
    config_file = Path(__file__).parent / 'config.yaml'
    return load(config_file.read_text(), CONFIG_SCHEMA).data


CONFIG = read_config()
