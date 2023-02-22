
import os
import sys
import logging
import configparser
from logging.handlers import RotatingFileHandler

_logs_directory = 'logs'
_config = configparser.ConfigParser()

def _get_logger():
    if not os.path.exists(_logs_directory):
        os.makedirs(_logs_directory)
    formatter = logging.Formatter('%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    file_handler = RotatingFileHandler(
        os.path.join(_logs_directory, 'records.log'), 
        maxBytes=1024*1024, 
        backupCount=10
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    logger = logging.getLogger('log')
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger

# Public

def config(file_path):
    global _config
    _config.read(file_path)
    return _config

logger = _get_logger()