#!/usr/bin/python3

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

def fetch_status(url):
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))

if __name__ == "__main__":
    fetch_status(url)
