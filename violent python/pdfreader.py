#!/usr/bin/python

import PyPDF2
import optparse
from PyPDF2 import PdfFileReader

def printMeta(fileName):
    pdfFile = PdfFileReader(file(fileName, 'rb'))
    docInfo = pdfFile.getDocumentInfo()
    print '[+] ***** PDF Meta Data *****'
    print '[+] #####'+fileName +'#####'
    for metaItem in docInfo:
        print '[+] '+metaItem+':'+docInfo[metaItem]

def main():
    parser = optparse.OptionParser('USage: %prog "+\" -f <pdf file name>')
    parser.add_option("-f", "--file", dest='fileName', help="specify a PDF to get the metadata from")
    (options, args) = parser.parse_args()
    fileName = options.fileName
    if fileName == None:
         print parser.USage
         exit(0)
    else:
        printMeta(fileName)
if __name__ == '__main__':
    main()
