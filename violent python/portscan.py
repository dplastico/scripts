import optparse
import socket
from socket import *

def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        print '[+]%d/tcp open'%tgtPort
        connSkt.close()
    except:
        print '[-]%d/tcp closed'%tgtPort

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print  '[-] Cannot resolve %s : Unknown host'%tgtPort
    try:
        tgtName = gethostbyaddr(tgtIP)
        print '\n[+] Scan results for: ' + tgtName[0]
    except:
        print '\n[+] Scan results for: ' + tgtIP
    
    setdefaulttimeout(1)
    for tgtPort in tgtPorts
    print 'Scaning port '+ tgtPort
    connScan(tgtHost, int(tgtPort))
        


parser = optparse.OptionParser('usage %prog -H ' +\
'<target host> -p <target port>')

parser.add_option('-H', dest='tgtHost', type='string', \
help = 'specify target host')

parser.add_option('-p', dest='tgtPort', type='int', \
help = 'specify target port')

(options, args) = parser.parse_args()
tgtHost = options.tgtHost
tgtPort = options.tgtPort
tgtPorts = str(options.tgtPort).split(',')

if (tgtHost == None)|(tgtPort == None):
    print parser.usage