from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
import sys

PORT = int(input("input port number: "))
ADDRESS = ('', PORT)

httpd = ThreadingHTTPServer(ADDRESS,SimpleHTTPRequestHandler)
print("Server is running!",ADDRESS,"\nPress Ctrl+C to stop the server.")

try:
    while True:
        httpd.serve_forever()
except KeyboardInterrupt:
    sys.exit()