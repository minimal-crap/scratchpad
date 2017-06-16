import os
import sys
import getpass
import socket
import threading
import select
from optparse import OptionParser

from minimal_logger import MinimalLogger


class MinimalShellHandler:
    """MinimalShellHandler to manage reverse shell from the machine."""

    def __init__(self,
                 ssh_port=None,
                 pkey_passphrase=None,
                 verbose_mode=False):
        self.user = os.getenv('USER')
        logger_params = {
            'file_name': 'error.log',
            'file_handler': True,
            'stream_handler': False,
        }
        self.logger_instance = MinimalLogger(**logger_params)
        try:
            if ssh_port is None:
                raise Exception("ssh port not defined")
            else:
                self.ssh_port = ssh_port
            self.pkey_passphrase = pkey_passphrase
            self.verbose_mode = verbose_mode
        except Exception as error:
            self.logger_instance.logger.error(
                "MinimalShellHandler::__init__:{}".format(
                    error.message
                )
            )

    def verbose(self):
    """"""
