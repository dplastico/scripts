import nmap
import sys
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
    nmscan = nmap.PortScanner()
    print target
    print port
    nmscan.scan(target, port, arguments=args_nmap)
    state = nmscan[target]['tcp'][int(port)]['state']
    print "[nmap_Scan]" + target + "tcp/"+port+""+state

nmapscan(target_host, target_port)
