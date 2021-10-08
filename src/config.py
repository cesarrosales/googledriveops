import json

with open('src/config.json') as json_config:
    config = json.load(json_config)

def c_gdrive_scopes():
    return config['gdrive']['scopes']

def c_source_folder():
    return config['gdrive']['sourcefolder']

def c_print_output():
    return config['printOutput']
