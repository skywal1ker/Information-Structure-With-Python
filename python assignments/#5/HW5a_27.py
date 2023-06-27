"""
27. A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in
a document. In the fields of computational linguistics and natural language processing,
it is common to disregard hapax legomena (and sometimes other infrequent words),
as they are likely to have little value for computational techniques. This disregard has
the added benefit of significantly reducing the memory use of an application. Define
a function that given the file name of a text will return all its hapaxes. Make sure your
program ignores capitalization.
"""


def hapax(name):
    count1 = 0
    ob = open(name,"r")
    x = ob.read().split(' ')
    ob.close()
    for i in range(len(x)):
        x[i] = x[i].lower()
    for i in range(len(x)):
        j = x[i]
        count = x.count(j)
        if(count == 1):
            count1 = count1+1
            
    print("words amount in example file: " + str(len(x)))
    print("hapaxes amount in example file: " + str(count1))
hapax("exam.txt")

