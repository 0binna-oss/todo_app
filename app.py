import http.server 
import socketserver 
import urllib.parse as urlparse 
import json 

task = []
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_get(self):
        if self.path == '/task':
            self.send_response(200)
            self.send_header('content-type','application/json')
            self.end_headers()
            self.wfile.write(json.dumps(task).encode())
        else:
            super().do_get()
    
    def do_POST(self):
        if self.path == '/add':
            content_lenght = int(self.headers['content-lenght'])
            post_data = self.rfile.read(content_lenght)
            task = urlparse.parse_qs(post_data.decode())['tasks'][0]
            task.append(task)
            self.send_response(303)
            self.send_header('location','/')
            self.end_headers()
        elif self.path.startswith('/delete/'):
            task.id = int(self.path.split('/')[-1])
            if 0 <= task.id < len(task):
                task.pop(task.id)
            self.send_response(303)
            self.send_header('location','/')
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()
#change the directory to where index.html are located 
handler_object = MyHttpRequestHandler
PORT = 8000
my_server = socketserver.TCPServer(("", PORT), handler_object)

print("serving on port{PORT}")
my_server.serve_forever()