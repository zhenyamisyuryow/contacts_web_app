from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from controller import ContactController




class RequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        controller = ContactController()
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(controller.get_contacts().encode())
        elif self.path.startswith('/edit/'):
            index = int(self.path.split('/')[-1][0])
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(controller.edit_contact(index).encode())
    
    def do_POST(self):
        controller = ContactController()
        if self.path == '/create':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            params = parse_qs(post_data)
            self.send_response(201)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(controller.add_contact(params).encode())

        elif self.path.startswith('/edit/'):
            index = int(self.path.split('/')[-1][0])
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            params = parse_qs(post_data)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(controller.update_contact(index, params).encode())

        elif self.path.startswith('/delete/'):
            index = int(self.path.split('/')[-1][0])
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(controller.delete_contact(index).encode())

    
def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Server running at http://localhost:8000')
    httpd.serve_forever()

if __name__ == '__main__':
    run()