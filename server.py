from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

from controllers import list_contacts, create_contact, edit_contact, update_contact, delete_contact, generate_error_page

# def generate_error_page(error_message):
#     return f"""
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>Error</title>
#         <script>
#             setTimeout(function() {{
#                 window.location.href = '/';
#             }}, 5000); // Redirect after 5 seconds
#         </script>
#     </head>
#     <body>
#         <h1>Error</h1>
#         <p>{error_message}</p>
#         <p>Redirecting to homepage...</p>
#     </body>
#     </html>
#     """


class ContactListHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(list_contacts().encode())
        elif self.path.startswith('/edit/'):
            index = int(self.path.split('/')[-1][0])
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(edit_contact(index).encode())

    def do_POST(self):
        if self.path == '/create':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            params = parse_qs(post_data)
            error_message = create_contact(params)
            if error_message:
                self.send_response(400)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(generate_error_page(error_message).encode())
                return
            self.send_response(303)
            self.send_header('Location', '/')
            self.end_headers()
        elif self.path.startswith('/update/'):
            index = int(self.path.split('/')[-1])
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            params = parse_qs(post_data)
            error_message = update_contact(index, params)
            if error_message:
                self.send_response(400)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(generate_error_page(error_message).encode())
                return
            self.send_response(303)
            self.send_header('Location', '/')
            self.end_headers()
        elif self.path.startswith('/delete/'):
            index = int(self.path.split('/')[-1])
            error_message = delete_contact(index)
            if error_message:
                self.send_response(400)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(generate_error_page(error_message).encode())
                return
            self.send_response(303)
            self.send_header('Location', '/')
            self.end_headers()


def run_server():
    server_address = ('', 5000)
    httpd = HTTPServer(server_address, ContactListHandler)
    print('Server running at http://localhost:5000')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
