"""
11. A Caesar cipher encrypts a message by shifting letters in the alphabet. For example, a
shift of 4 maps 'a' to 'e' and maps 'p' to 't' Here is a famous line from Shakespeare
encrypted with a shift of 4: 'vq dg qt pqv vq dg: vjcv ku vjg swguvkqp.'
(a) Write a program that takes as input a string to be encrypted and an integer encrpytion
shift (such as 4 mentioned earlier), and prints the encrypted string. [Hint: zip()
is helpful in building a dictionary. Also, remember to handle space–it doesn’t shift].
(b) Extend your program to take an additional input that indicates if your program is
to encrypt or decrypt the string.

"""

def encrypt(string, shift, dic):
    encrypted = ""
    for char in string:
        if char not in dic.keys():
            encrypted += char
            continue
        index = dic[char]
        index = (index+shift)%26
        encrypted += list(dic.keys())[list(dic.values()).index(index)]
        
    return encrypted
    


print("1. Encryption")


string = input("Enter the string to encrypt: ")
shift = int(input("Enter the integer shift for encryption: "))

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
dic = dict(zip(alphabets, index))

encrypted = encrypt(string, shift, dic)
print("Encrypted string: {}".format(encrypted))