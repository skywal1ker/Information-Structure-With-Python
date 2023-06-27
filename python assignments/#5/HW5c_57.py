"""
57. The letters a, b, d, e, B, o, p, and q all have something in common: a hole. If you imagine
that the letters were made of stretchy material such as rubber, you could transform
one letter into another while preserving the hole. If tearing or gluing are not allowed
no other letter (without a hole) could be transformed by stretching into one of these
letters with holes. Mathemeticans say that these letters are topologically similar: One sel
has a hole, the rest do not.
(a) Write a function that takes as an argument a lowercase string and finds the counts
of letters in the string with holes and and a count of letters without holes.
b) Write a function that searches a word list and prints all the words that have two or
more letters with holes.
(e) The set of uppercase letters with holes is different from the set of lowercase letters,
e.g, lowercase "e" belongs to the set of letters with a hole, but its capital "E" does
not. Refactor your functions to consider uppercase letters.
"""
def c_holes(s):
    holes=["a","b","d","e","g","o","p","q","A", "B", "D", "O", "P", "Q", "R"]
    u_holes = ["A", "B", "D", "O", "P", "Q", "R"]
    c_holes = 0
    c_u_holes = 0
    for element in s:
        if element in holes:
            c_holes = c_holes + 1
        if element in u_holes:
            c_u_holes = c_u_holes + 1
    no_holes = len(s) - c_holes
    return c_holes,no_holes,c_u_holes

def word_holes(input):
    holes = ['a', 'b', 'd', 'e', 'g', 'o', 'p', 'q']
    for element in input.split(" "):
        count = sum([element.count(k) for k in holes])
        if count>=2:
            print(element)
print("Type the sentence: ")
inp_str = input()
t = c_holes(inp_str)
print("amount of letters with holes are: " + str(t[0]))
print("amount of letters without holes are: " + str(t[1]))
print("List of words with holes and two or more letters are\n")
(word_holes(inp_str))
print("Upper case letters with holes are: " + str(t[2]))
