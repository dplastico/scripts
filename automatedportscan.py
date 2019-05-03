#!/usr/bin/env python
import nmap
import sys
import masscan

#import socket
if len(sys.argv) !=3:
    print "[*] Usage: %prog <Target IP> <output file>"
    sys.exit(1)

target_host = sys.argv[1]
#print target
output = sys.argv[2]
#print output
args_nmap = "-sV -sC -oN "+output
target_port = "80"
def nmapscan (target, port):
    #aca loop para leer los puertos
    nmscan = nmap.PortScanner()
    print target
    print port
    nmscan.scan(target, port, arguments=args_nmap)
    state = nmscan[target]['tcp'][int(port)]['state']
    print "[nmap_Scan]" + target + "tcp/"+port+""+state

def mass (target_host):
    mass_scan = masscan.PortScanner()
    mass_scan.scan(target_host, arguments='--rate=1000 -e tun0')
    print "masscan..................."
    #aca crear archivo leible por nmap
    print mass_scan



mass('10.10.10.130')
