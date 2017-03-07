import crypt


def testPass(cryptPass):
#    import pdb; pdb.set_trace()  # XXX BREAKPOINT
    salt = cryptPass[0:2]
    dictFile = open('dictionary.txt','r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word,salt)
        if (cryptWord == cryptPass):
            print "[+] Found Password: "+word+"\n"
            return
    print "[-] Password Not Found.\n"
    return

def main():
    passFile = open('password.txt')
    for line in passFile.readlines():
        if ":" in line:
                user = line.split(':')[0]
                cryptPass = line.split(':')[1].strip(' ')
                print "[*] Cracking Password For: "+user
                testPass(cryptPass)

def hello():
    """docstring for hello"""
    hello.func_code()
    hello.__name__()


if __name__ == "__main__":
    main()

