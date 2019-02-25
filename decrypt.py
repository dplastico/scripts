import crypt

def testpass(cryptpass):
    salt = cryptpass.[0:2]
    dictfile = open('dictionary.txt', 'r')
    for word in dictfile.readlines():
        word =  word.strip('\n')
        cryptword = crypt.crypt(word,salt)
        if (cryptword == cryptpass):
            print "[+] found password: "+ word + "\n"
            return
        print "[-] Password not found. \n"
        return
def main():
    passfile = open('password.txt')
    for line in passfile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptpass = line.splipt(':')[1].strip(' ')
            print "cracking password for user: "+ user
            testpass(cryptpass)
if __name__ == '__main__':
    main()



