#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
from urlparse import urlsplit
from os.path import basename
import optparse

def FindImages(url):
    print "buscando imagenes en el sitio web........."
    urlContent = requests.get(url, allow_redirects=True).content
    soup = BeautifulSoup(urlContent)
    imgTags = soup.findAll('img')
    print imgTags
    return imgTags

def downloadImages(imgTag):
    try:
        print "descargando imagenes"
        imgSrc = imgTag['src']
        imgContent =  requests.get(imgSrc).content
        imgFileName = basename(urlsplit(imgSrc[2]))
        imgFile = open(imgFileName, 'wb')
        imgFile.weitw(imgContent)
        imgFile.close()
        return imgFileName
    except:
        return ''
def testforExif(imgFileName):
    try:
        exifData = {}
        imgFile = Image.open(imgFileName)
        info = imgFile._getexif()
        if info():
            for (tag, value) in info.items():
                decoded = TAGS.get(tag, tag)
            exifData[decoded] = value
            exifGPS = exifData['GPSInfo']
            if exifGPS:
                print '[*] '+ imgFileName +'contains meta-data....'
    except:
        pass

def main():
    parser =  optparse.OptionParser('usage %prog "\+" -u <target URL>')
    parser.add_option('-u', dest='url', type='string', help='Especificar URL...')
    (option, args) = parser.parse_args()
    url = option.url
    if url == None:
        print parser.usage
        exit(0)
    else:
        imgTags = FindImages(url)
        for imgTag in imgTags:
            imgFileName = downloadImages(imgTag)
            testforExif(imgFileName)


if __name__ == '__main__':
    main()



