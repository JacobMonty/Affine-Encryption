#Encryption program for Affine cypher

from math import gcd

def ENCRYPTION(PlainText, Alpha, Beta):

    Alpha = int(Alpha)
    Beta = int(Beta)


    CYPHER = ""

    for char in PlainText:
        if char.isalpha():
            char = char.lower()
            flee = ord(char) - ord('a')


            Encryptformula = (Alpha * flee + Beta) % 26

            Encryptcharacter = chr(Encryptformula + ord('a'))

            CYPHER += Encryptcharacter
        else:
            CYPHER += Encryptcharacter

    return CYPHER


Alpha = input("Please input the A key for the Affine Cipher: ")
Beta = input ("Please input the B key for the Affine Cipher: ")

PlainText = input ("Please input the Plaintext to encrypt: ")




CYPHER = ENCRYPTION(PlainText, Alpha, Beta)



print("Encrypted text: ", CYPHER)
