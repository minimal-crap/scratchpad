import os


LOG_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir,
    os.pardir,
    'logs'
))

CONFIG_FILE_PATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir,
    os.pardir,
    'config.txt'
))

CRON_SCRIPTS_PATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir,
    'cron_scripts'
))
