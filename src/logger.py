import logging
import uuid
from datetime import datetime

transaction = uuid.uuid4()

def configure():
    script_log_info('configuring logger...')
    logging.basicConfig(filename='logs.log', level=logging.DEBUG)

def script_log_info(s):
    log = f'[{transaction}][{datetime.now()}]: {s}'
    logging.info(log)
    print(log)

def script_log_warning(s):
    log = f'[{transaction}][{datetime.now()}]: {s}'
    logging.warning(log)
    print(log)

def script_log_error(s):
    log = f'[{transaction}][{datetime.now()}]: {s}'
    logging.error(log)
    print(log)

def script_log_debug(s):
    log = f'[{transaction}][{datetime.now()}]: {s}'
    logging.debug(log)
    print(log)

configure()