# from .route import Route

class Router():
    _instance = None
    """Singleton Router class to manage routes."""

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Router, cls).__new__(cls)
            cls._instance.routes = {}
        return cls._instance

    def route(self, method: str, path: str):
        """Decorator to register a route."""
        def wrapper(func):
            self.routes[(method.upper(), path)] = func
            return func
        return wrapper

    def dispatch(self, method: str, path: str, handler):
        """Dispatch the request to the appropriate route."""
        key = (method.upper(), path)
        func = self.routes.get(key)
        if func:
            return func(handler)
        else:
            handler.send_response(404)
            handler.end_headers()
            handler.wfile.write(b"404 Not Found")
            return None