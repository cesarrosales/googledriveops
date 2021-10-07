import json
from logger import script_log_info, script_log_error

with open('config.json') as json_config:
    config = json.load(json_config)

def c_gdrive_scopes():
    return config['gdrive']['scopes']
