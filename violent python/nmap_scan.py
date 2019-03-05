import nmap
import optparse

def nmapScan (tgtHost, tgtPort):
    nmScan = nmap.PortScanner()
    nmScan.Scan(tgtHost, tgtPort)
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    print "[*]" + tgtHost + "tcp/"+tgtPort+""+state
def main():
    parser = optparse.OptionParser('usage%prog'+\
    '-H <target host> -p <target Port>')

    parser.add_option('-H', dest='tgtHost',type='string',\
    help='Specify Host')

    parser.add_option('-p', dest='tgtPort',type='string',\
    help='Specify Ports separated by comma')

    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost==None)|(tgtPorts[0]==None):
        print parser.usage
        exit(0)
    for tgtPort in tgtPorts:
        nmapScan(tgtHost, tgtPort)
if __name__ == '__main__':
    main()
