import zipfile

def extractFile (zFile, password):
    try:
        zFile.extractall(pwd = password)
        return password
    except:
        return

def main():
    zFile = zipfile.ZipFile('evil.zip')
    passfile = open('dictionary.txt')
    for line in passfile:
        password = line.strip('\n')
        guess = extractFile(zFile, password)
        if guess:
            print '[+] password = ' + password + '\n'
            exit(0)
        else:
            print 'NO HAY PASSWORD'
if __name__ == '__main__':
    main()
