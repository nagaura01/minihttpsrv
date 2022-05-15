from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
import sys

PORT = int(input("input port number: "))

httpd = ThreadingHTTPServer(('',PORT),SimpleHTTPRequestHandler)
print("Server is running! http://localhost:"+str(PORT)+"\nPress Ctrl+C to stop the server.")

try:
    while True:
        httpd.serve_forever()
except KeyboardInterrupt:
    sys.exit()