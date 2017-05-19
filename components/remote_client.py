
from tornado.ioloop import IOLoop
from tornado.websocket import WebSocketHandler
from tornado.web import Application


class ClientSocketHandler(WebSocketHandler):
    """ClientSocketHandler to handle client sockets."""

    def check_origin(self, origin):
        """check_origin method to check origin of the client."""
        return True

    def open(self):
        """
        open method,
        an event handler for when client opens a socket with server.
        """
        pass

    def on_message(self):
        """
        on_message method,
        an event handler for when server receives message from client.
        """
        pass

    def on_close(self):
        """
        on_close method,
        an event handler for when client closes connection.
        """
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
        
