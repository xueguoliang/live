
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

class MyHttpHander(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write('not support'.encode())

    def do_POST(self):
        self.send_response(200)
        self.end_headers()

        cLen = int(self.headers['content-length'])
        rLen = 0
        msg = b''

        while rLen != cLen:
            data = self.rfile.read(cLen - rLen)
            if not data:
                break
            msg += data
            rLen += len(data)

        msg = msg.decode()

        self.handleData(msg)

def startServer(port, handleClass):
    serverAddr = ('', port)
    httpd = HTTPServer(serverAddr, handleClass)
    httpd.serve_forever()

