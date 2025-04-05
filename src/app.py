import sys
from socketserver import TCPServer
from src.route import Router
from src.handlers import CustomRequestHandler
from src.template import JinjaTemplate
from src.hotreloader import HotReloader


class App():
    def __init__(
        self, 
        host: str = "localhost",
        port: int = 9999,
        handler_class=CustomRequestHandler,
        server_class=TCPServer,
        static_dir: str = "static",
        router_class: object = Router,
        template_engine: object = JinjaTemplate,
        hot_reload: object = HotReloader,
    ):
        self.host = host
        self.port = port
        self.handler_class = handler_class
        self.server_class = server_class
        self.static_dir = static_dir
        self.router = router_class()
        self.template_engine = template_engine()
        self.hot_reload = hot_reload()
    

    def run(self):
        """Run the server."""
        def _start():
            with self.server_class((self.host, self.port), self.handler_class) as server:
                print(f"🚀 Serving at http://{self.host}:{self.port}")
                server.serve_forever()

        if self.hot_reload:
            print("🔄 Auto-reload enabled.")
            self.hot_reload.start(_start)
        else:
            try:
                _start()
            except KeyboardInterrupt:
                print("\n🛑 Server interrupted. Shutting down.")
                sys.exit(0)

    @property
    def route(self):
        """Decorator to register a route."""
        return self.router.route

