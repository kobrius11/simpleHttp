from http.server import BaseHTTPRequestHandler
import shutil
from pathlib import Path


class EchoRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)

    def copyfile(self, src, out):
        """Copy all data between two file objects."""
        shutil.copyfileobj(src, out)

    def log_message(self, format, *args):
        """Log an arbitrary message to stdout."""
        print("%s - - [%s] %s\n" %
              (self.client_address[0],
               self.log_date_time_string(),
               format % args))
    
    def get_template(self, template_name: str) -> Path:
        """Get the template file path."""
        return Path(__file__).parent / "static" / template_name

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        with open(self.get_template('index.html'), "rb") as f:
            self.copyfile(f, self.wfile)