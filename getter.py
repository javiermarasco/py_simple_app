from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import time
import requests

dest_url = 'http://localhost' #os.getenv('DEST_URL')

while True:
    response = requests.get(url=dest_url)
    print(response.text)
    time.sleep(10)
