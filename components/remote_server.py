from tornado.ioloop import IOLoop
from tornado.websocket import WebSocketHandler
from tornado.web import Application

from lib.minimal_logger import MinimalLogger


class ClientSocketHandler(WebSocketHandler):
    """ClientSocketHandler to handle client sockets."""

    def __init__(self):
        socket_info_logger_params = dict()
        socket_info_logger_params['file_name'] = 'socket_server_info.log'
        socket_info_logger_params['file_handler'] = True
        socket_info_logger_params['stream_handler'] = True
        self.socket_server_info_logger = MinimalLogger(
            **socket_info_logger_params)

    def check_origin(self, origin):
        """check_origin method to check origin of the client."""
        return True

    def open(self):
        """
        open method,
        an event handler for when client opens a socket with server.
        """
        self.socket_server_info_logger.logger.info(
            "remote_server :: ClientSocketHandler :: open : {}".format(
                "new client connected"
            )
        )

    def on_message(self, message):
        """
        on_message method,
        an event handler for when server receives message from client.
        """
        self.socket_server_info_logger.logger.info(
            "remote_server :: ClientSocketHandler :: on_message : {}".format(
                message
            )
        )

    def on_close(self):
        """
        on_close method,
        an event handler for when client closes connection.
        """
        self.socket_server_info_logger.logger.info(
            "remote_server :: ClientSocketHandler :: on_close : {}".format(
                "client connection closed."
            )
        )
        pass


class MainApplicaion(Application):
    """
    MainApplication class,
    defines all routes for socket client api.
    """

    def __init__(self):
        handlers = [
            (r"/", ClientSocketHandler)
        ]

        # calling super class' init method
        Application.__init__(self, handlers)


def main():
    """
    main method, initiates app instances
    and start client socket handler.
    """
    err_logger_params = dict()
    err_logger_params['file_name'] = 'socket_server_err.log'
    err_logger_params['stream_handler'] = False
    err_logger_params['file_handler'] = True
    socket_serer_err_logger = MinimalLogger(**err_logger_params)

    try:
        app_instance = MainApplicaion()
        app_instance.listen('8001', address='localhost')
        IOLoop.instance().start()

    except Exception as err:
        socket_serer_err_logger.logger.error(
            "remote_server :: main : {}".format(
                err.message)
        )


if __name__ == '__main__':
    main()
