from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import time
import requests
import json

# dest_url = "http://localhost:30000" #os.getenv('DEST_URL')

loop_wait_time = os.getenv('LOOPWAITTIME')
inputs = json.loads(os.getenv('INPUT'))

#urls = inputs.urls  

while True:
    for input in inputs:
        response = requests.get(url=input['url'])
        print(f"getting from {input['url']} and now waiting {input['cadence']} seconds to get the next url.")
        time.sleep(int(input['cadence']))
        print(f"Waiting {int(loop_wait_time)} seconds before next loop.")
    time.sleep(int(loop_wait_time))
