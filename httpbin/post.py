#!/usr/bin/python
import sys
import requests

if len(sys.argv) < 2:
    print "usalo bien"
    sys.exit(1)

url = sys.argv[1]
payload = {'username':'user', 'password':'pass'}
response = requests.post(url, data=payload)

jsonresponse = response.json()

print jsonresponse['form']