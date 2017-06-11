import os
import getpass

from crontab import CronTab

import settings
from minimal_logger import MinimalLogger


class MinimalCronHandler:
    """MinimalCronHandler class to handle cron tasks."""

    def __init__(self,
                 scripts_dir=None,
                 script_name=None,
                 interpreter_path=None,
                 output_path=None):
        """MinimalCronHandler class init method"""
        logger_params = {
            'file_name': 'error.log',
            'file_handler': True,
            'stream_handler': False,
        }
        self.logger_instance = MinimalLogger(**logger_params)
        try:
            self.cron = None
            self.cron_job = None
            # checking if mandatory path has been provided
            if scripts_dir is not None:
                self.scripts_dir = scripts_dir
            else:
                self.scripts_dir = settings.CRON_SCRIPTS_PATH

            if script_name is not None:
                self.script_name = script_name
            else:
                raise Exception("cron script name not defined.")

            if interpreter_path is not None:
                self.interpreter_path = interpreter_path
            else:
                raise Exception("cron script interpreter path not defined")

            if output_path is not None:
                self.output_path = output_path
            else:
                self.output_path = None

            # checking if supplied paths exist
            if not os.path.exists(self.scripts_dir):
                raise Exception("invalid cron scripts directory")

            if not os.path.exists(self.interpreter_path):
                raise Exception("invalid cron scripts interpreter path")

            if self.output_path is not None and not os.path.exists(
                    self.output_path):
                raise Exception("invalid cron scripts output path")

        except Exception as error:
            self.logger_instance.logger.error(
                "MinimalCronHandler::__init__:{}".format(error.message))

    def prepare_command(self):
        """Prepare cron task command from provided variables"""
        try:
            script_absolute_path = os.path.join(self.scripts_dir,
                                                self.script_name)

            if not os.path.exists(script_absolute_path):
                raise Exception("invalid cron task script path")

            if self.output_path is not None:
                cron_command = "{} {} >> {}".format(
                    self.interpreter_path,
                    script_absolute_path,
                    self.output_path
                )
            else:
                cron_command = "{} {}".format(
                    self.interpreter_path,
                    script_absolute_path)

            return cron_command

        except Exception as error:
            self.logger_instance.logger.error(
                "MinimalCronHandler::prepare_command:{}".format(error.message))

    def prepare_execution_frequency(self, frequency_param=None, command=None):
        """Prepares the frequency at which cron tasks are executed."""
        try:
            if frequency_param is None:
                raise Exception('frequency parameter not provided')
            self.cron = CronTab(user=getpass.getuser())
            self.cron_job = self.cron.new(command=command)
            self.cron_job.setall(frequency_param)
            return self.cron_job.is_valid()
        except Exception as error:
            self.logger_instance.logger.error(
                "MinimalCronHandler::prepare_execution_frequency:{}".format(
                    error.message
                )
            )

    def add_cron_task(self):
        """Adds the cron task command to crontab file."""
        try:
            self.cron.write_to_user()
        except Exception as error:
            self.logger_instance.logger.error(
                "MinimalCronHandler::add_cron_task:{}".format(
                    error.message
                )
            )
