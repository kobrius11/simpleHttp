from http.server import BaseHTTPRequestHandler
from src import dependancy_injector
# from src.template import BaseTemplate
from src.route import Router


class CustomRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)

    @dependancy_injector(Router)
    def do_GET(self, router):
        router.dispatch("GET", self.path, self)
    