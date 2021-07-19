import getopt
import secrets
import string
import sys
import time

def math_err():
    print("Number of pieces cannot exceed length of password. One lowercase letter is included by default.")
    exit(1)

def usage():
    print("Please use the following options:\n'-l', '--length' is the required length of the pasword to generate.\n'-h', '--help', '-u', '--usage' is for this loveley menu.\n\nYou will be prompted for the following:\n  min number of uppercase letters.\n  min number of numeric digits.\n  min number of punctuation characters.\nAll characters default to 0 with the exception of lowercase letters.\n\nPlease note that the resulting passwords have AT LEAST as many of the required complexity values as specified.")

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "l:t:hu", ["length=", "token=", "help", "usage"])
    except getopt.GetoptError as err:
        usage()
        sys.exit(2)
    for o, a in opts:
        if o in ("-h", "--help", "-u", "--usage"):
            usage()
            sys.exit()
        # cycle 7 starter
        if o in ("-l", "--length"):
            # length = 15
            pswd = ''
            alpha = 1
            numeric = 1
            punct = 1
            
            length = a
            length = 15 if length == '' else int(length)
            # print(str(length))
            pswd += string.ascii_letters

            alpha = input("Enter the minimum amount of uppercase letters: ")
            alpha = 1 if alpha == '' else int(alpha)
            if alpha >= length: math_err()

            numeric = input("Enter the minimum amount of digits: ")
            numeric = 1 if numeric == '' else int(numeric)
            if numeric == '': numeric = 1
            if numeric >0:
                pswd += string.digits
                if numeric >= length: math_err()

            punct = input("Enter the minimum amount of punctuation/special characters: ")
            punct = 1 if punct == '' else int(punct)
            if punct == '': punct = 1
            if punct >0:
                pswd += string.punctuation
                if punct >= length: math_err()

            if numeric + punct + alpha > length: math_err()
            # print(alpha, numeric, punct, length)
            counter = 0
            start = time.time()
            while True:
                counter += 1
                password = ''.join(secrets.choice(pswd) for i in range(length))
                if (any(x.islower() for x in password)
                        and sum(x.isupper() for x in password) >= alpha
                        and sum(x.isdigit() for x in password) >= numeric
                        and sum(x in string.punctuation for x in password) >= punct ):
                    print("Generated password: ", password)
                    print("Throw away password counter: " + str(counter) + " in " + str(time.time() - start) + " seconds")
                    break
        # token section
        if o in ("-t", "--token"):
            length = input("What is the desired length of your token: ")
            length = 15 if length == '' else int(length)
            if a == "bytes":
                password = secrets.token_bytes(length)
            if a == "hex":
                password = secrets.token_hex(length)
            if a == "url":
                password = secrets.token_urlsafe(length)
            print(password)


if __name__ == '__main__':
    main()
    exit(0)
