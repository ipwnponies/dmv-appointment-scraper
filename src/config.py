import os
import yaml


def read_config():
    with open(os.path.join(os.path.dirname(__file__), 'config.yaml'), 'r') as f:
        return yaml.load(f)

config = read_config()
