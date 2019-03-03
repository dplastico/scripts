import optparse
from socket import *
from threading import *

screenLock = Semaphore(value=1)

def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        ConnSkt.send('dplastico\r\n')
        results = connSkt.recv(100)
        screenLock.acquire()
        print '[+]%d/tcp open'%tgtPort
        print '[+] '+ str(results) 
        connSkt.close()
    except:
        screenLock.acquire()
        print '[-]%d/tcp closed'%tgtPort
    finally:
        screenLock.release()
        connSkt.close()
    
def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print  '[-] Cannot resolve %s : Unknown host'%tgtPort
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print '\n[+] Scan results for: ' + tgtName[0]
    except:
        print '\n[+] Scan results for: ' + tgtIP
    
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target = connScan, args=(tgtHost, int(tgtPort)))
        t.start()
        print 'Scaning port '+ tgtPort
        connScan(tgtHost, int(tgtPort))
        

def main():
    parser = optparse.OptionParser('usage %prog -H ' +\
    '<target host> -p <target port>')

    parser.add_option('-H', dest='tgtHost', type='string', \
    help = 'specify target host')

    parser.add_option('-p', dest='tgtPort', type='int', \
    help = 'specify target port[s] separated by comma')

    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    #tgtPort = options.tgtPort
    tgtPorts = str(options.tgtPort).split(',')

    if (tgtHost == None)|(tgtPorts[0] == None):
        print ' [-] You must specify a host and a port[s]. '
        #print parser.usage

    portScan(tgtHost, tgtPorts)
if __name__ == '__main__':
    main()

