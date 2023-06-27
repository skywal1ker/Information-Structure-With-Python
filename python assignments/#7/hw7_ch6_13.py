"""
13. Find a text file online that contains the English dictionary. Write a program that cycles
through this text file to find compound words. Your program should return these compound words along with the two words that compose it. For example, a “raincoat”
is a compound word so your program should return raincoat = rain + coat.
"""


from collections import deque

temp=open("C:/users/skywalker/desktop/sai.dic","r")
tup1 = []
d = deque()
for str in temp:
    tup1.append(str)
    d.append(str)
for word in tup1:
    for i in range(len(word)):
        word.strip()
        s1 = word[0:i]
        s2 = word[i:len(word)]
        s1.strip()
        s2.strip()
        print(s1,s2)
        if (s1 in temp) and (52 in temp):
            print(word," ", s1 ,"+", s2)
            temp.close()