import sys
import math

def main():
    b1chars = input("Entrez les caractères de la base de départ: ")
    b1 = list(b1chars)
    if len(b1) > len(set(b1)):
        print("Erreur: tout les caractères de la base doivent être uniques.")
        sys.exit(1)
    print("(base %d enregistrée)"%len(b1))
    b2chars = input("Entez les caractères de la base d'arrivée: ")
    b2 = list(b2chars)
    if len(b2) > len(set(b2)):
        print("Erreur: tout les caractères de la base doivent être uniques.")
        sys.exit(1)
    print("(base %d enregistrée)"%len(b2))
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
                print("Error: caractère non reconnu dans la base de départ (%s)"%c)
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
