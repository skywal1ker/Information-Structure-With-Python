"""
51. Write a program that prompts for the user to input a sentence. Then check this sentence
to make sure the first word of the sentence is capitalized and the sentence ends with a
punctuation mark. If it is not properly written, fix the sentence, print the type of error,
and print the fixed sentence.
"""
import string
import copy

str_txt = input("Please type the sentence: ")
count = lambda a,b:len(list(filter(lambda c: c in b,a)))
no_punc = count(str_txt,string.punctuation)
str_finish = copy.deepcopy(str_txt)
if str_txt[0].isupper() == False:
   print("Not started with a capital letter , it started with: ", str_txt[0])
   str_finish = str_txt.capitalize()
if (str_txt.endswith('.') == False):
   str_finish = str_finish + "."
print(str_finish)