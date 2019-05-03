#!/usr/bin/python
import sys
import nmap
import os


hosts = raw_input('Enter a hostname file to read from : ')
outnmap = raw_input('Enter a name for  nmap output files : ')
outdirb = raw_input('Enter a name for  dirb output files : ')
outnikto = raw_input('Enter a name for  nikto output files : ')
hosts = open("hosts.txt", 'r')

#host = '192.168.1.182'
def nmapscan(host):
    args_nmap = "-sV -T4 -Pn -oN "+str(host)+"-"+outnmap+".txt"
    scan = nmap.PortScanner()
    total = scan.scan(host, arguments=args_nmap) 
    #print scan[host].has_tcp(80)
        
    if scan[host].has_tcp(80) == True:
        print "http encontrado en "+host
        print "####################"
        print "####################"
        dirb(host)
        nikto(host)
     
    if scan[host].has_tcp(443) == True:
        print "http encontrado en "+host
        print "####################"
        print "####################"
        dirb(host)
        nikto(host)
 
def dirb(host):
    cmddirb = 'dirb http://'+host+'/ -o '+str(host)+outdirb+".txt"
    os.system(cmddirb)

def nikto(host):
    cmdnikto = 'nikto -h '+host+' -o '+str(host)+'-'+outnikto+".txt"
    os.system(cmdnikto)

for line in hosts:
    host = line.strip()
    print "***** Buscando host "+host+" *****"
    nmapscan(host)



