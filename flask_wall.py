from functools import wraps

__version__ = '0.1.0'


class SimpleWall:
    """Bypass a decorated flask route through a specified callback.

    Attributes:
        redirect_status_code (int): The status code that will returned to the client through the default callback.

    """

    def __init__(self, status_code=503):
        """Initialize the SimpleWall to bypass a decorated flask route completely.

        Args:
            status_code (int, optional): The status code that will returned to the client through the default callback. Defaults to 503.
        """
        self.redirect_status_code = status_code
        self._callback = None

        # set the internal callback attribute to the default callback function
        self.callback(self.default_callback)


    def callback(self, f):
        """Specify the function that will be executed when a flask route is restricted through the SimpleWall.

        Args:
            f (function): The function that will be executed.
        """
        self._callback = f

    
    def default_callback(self):
        """The default callback that will be executed if a callback is not defined through the @callback decorator.

        Returns:
            str: The body of the response sent to the client.
            int: The status code of the response sent to the client.
        """
        return 'Temporarily unavailable', self.redirect_status_code


    def restrict(self, f):
        """A decorator for flask routes that bypasses the route and executes _callback.

        Args:
            f (function): Theflask route that will be bypassed.

        Returns:
            function: The wrapper function that executes the callback.
        """
        @wraps(f)
        def wrapper(*args, **kwargs):
            return self._callback()
        return wrapper
