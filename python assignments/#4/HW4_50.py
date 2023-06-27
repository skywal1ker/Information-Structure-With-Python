"""
50. Develop a Python program that will: (1) prompt for input, (2) extract all the vowels
in the input string and make them lowercase, (3) add all the nonduplicate vowels you
found into a temporary string, and (4) stop the code when you have collected all five
vowels (aeiou) and print the number of trials that you did to collect all five vowel
characters.
"""
str_txt = input("Type the sentence please: ")
zero_vowels = []
vowel = []
count = 0
for operation in str_txt:
   if operation == "A" or "a" or operation == "E" or "e" or operation == "I" or "i" or operation == "O" or "o" or operation == "U" or "u":
         if(operation not in vowel):
            vowel.append(operation)
            if("a" in vowel and "e" in vowel and "i" in vowel and "o" in vowel and "u" in vowel):
                   break
   else:
         if(operation not in zero_vowels):
            zero_vowels.append(operation)
   count += 1
not_vowels = ''.join(zero_vowels)
vowels = ''.join(vowel)
vowels = str.lower(vowels)
vowels = list(set(vowels))

print("Other than vowels {}: All vowels: {}, All iterations.{}".format(str(not_vowels),str(vowels),str(count)))