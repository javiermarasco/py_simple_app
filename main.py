from http.server import BaseHTTPRequestHandler, HTTPServer
import os

hostname = "0.0.0.0"
port = os.getenv('PORT')

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.message = os.getenv('MESSAGE')
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(" Message ==> " + self.message, encoding='utf-8') )

runningServer = HTTPServer((hostname, port), Server)
print("Web server started.")

try:
    runningServer.serve_forever()
except KeyboardInterrupt:
    pass

runningServer.server_close()
print("Web server stopped.")
