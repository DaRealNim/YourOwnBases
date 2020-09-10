import sys
import math

def main():
    b1chars = input("Enter characters for the base to convert from: ")
    b1 = list(b1chars)
    if len(b1) > len(set(b1)):
        print("Error: all characters must be unique.")
        sys.exit(1)
    print("(base %d loaded)"%len(b1))
    b2chars = input("Enter characters for the base to convert to: ")
    b2 = list(b2chars)
    if len(b2) > len(set(b2)):
        print("Error: all characters must be unique.")
        sys.exit(1)
    print("(base %d loaded)"%len(b2))
    print("")
    while True:
        inp = input(">")
        if inp == "":
            continue

        #Conversion en bd -> base10
        input_to_b10 = 0
        p = 0
        for c in inp[::-1]:
            if not c in b1:
                print("Error: unknown character in starting base (%s)"%c)
                continue
            input_to_b10 += int(b1.index(c)*math.pow(len(b1), p))
            p+=1

        #conversion base10 -> ba
        realbase = len(b2)
        out = ""
        while input_to_b10 > 0:
            out = b2[input_to_b10%realbase] + out
            input_to_b10 = input_to_b10//realbase
        print(out)








if __name__ == '__main__':
    main()
