from configparser import ConfigParser

from settings import CONFIG_FILE_PATH, LOG_DIR
from minimal_logger import MinimalLogger


class MinimalConfiguration:
    def __init__(self, config_file_path=None):
        self.config_parser = ConfigParser()
        if config_file_path is None:
            self.config_file_path = CONFIG_FILE_PATH
        self.config_parser.read(self.config_file_path)

        logger_params = {
            'file_name': 'error.log',
            'file_handler': True,
            'stream_handler': False,
        }
        self.logger_instance = MinimalLogger(**logger_params)

    def get_config_value(section=None, key=None):
        """Fetch value of particular key from particular section."""
        try:
            # do the needful
        except Exception as error:
            self.logger_instance.logger.error(
            "MinimalConfiguration::get_config_value:{}".format(error.message))
