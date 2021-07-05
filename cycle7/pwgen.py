import getopt
import secrets
import string
import sys

def usage():
    print("Please use the following options:\n'-l', '--length' is the required length of the pasword to generate.\n'-h', '--help', '-u', '--usage' is for this loveley menu.\n\nYou will be prompted for the following:\n  min number of uppercase letters.\n  min number of numeric digits.\n  min number of punctuation characters.\nAll characters default to 0 with the exception of lowercase letters.\n\nPlease note that the resulting passwords have AT LEAST as many of the required complexity values as specified.")

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "l:hu", ["length=", "help", "usage"])
    except getopt.GetoptError as err:
        usage()
        sys.exit(2)
    length = 0
    pswd = ''
    alpha = 0
    numeric = 0
    punct = 0
    for o, a in opts:
        if o in ("-l", "--length"):
            length = int(a, 10)
            pswd += string.ascii_letters
        if o in ("-h", "--help", "-u", "--usage"):
            usage()
            sys.exit()

    alpha = int(input("Enter the minimum amount of uppercase letters: "))
            
    numeric = int(input("Enter the minimum amount of digits: "))
    if numeric >0:
        pswd += string.digits
            
    punct = int(input("Enter the minimum amount of punctuation/special characters: "))
    if punct >0:
        pswd += string.punctuation
    
    while True:
        password = ''.join(secrets.choice(pswd) for i in range(length))
        if (any(x.islower() for x in password)
                and sum(x.isupper() for x in password) >= alpha
                and sum(x.isdigit() for x in password) >= numeric
                and sum(x in string.punctuation for x in password) >= punct ):
            print(password)
            break



if __name__ == '__main__':
    main()
