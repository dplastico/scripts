#!/usr/bin/python
import requests
import sys

if len(sys.argv) < 2:
    print "usalo bien"
    sys.exit(1)

url = sys.argv[1]
payload = {"username":"user", "password":"pass"}

response = requests.get(url, params=payload)

print "***** PROBANDO *****\n", response.text
