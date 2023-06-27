
"""
44. Write a program that prompts for a sentence and calculates the number of uppercase
letters, lowercase letters, digits, and punctuation. Output the results neatly formatted
and labeled in columns.
"""
import string 
text_sentence = input("Please type the sentence: ")
upper_length=0
lower_length=0
digits=0
punctuation=0
for char in text_sentence:
   if char.isupper():
       upper_length +=1 
   if char.islower():
       lower_length +=1 
   if char.isnumeric():
       digits +=1 
   if char in string.punctuation:
       punctuation +=1

print("The number of upper length:",upper_length)
print("The number of lower length:",lower_length)
print("The number of digits:",digits)
print("The number of punctuation:",punctuation)

