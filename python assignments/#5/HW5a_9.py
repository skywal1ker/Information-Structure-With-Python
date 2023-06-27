"""
9. Write a function that takes as input an English sentence (a string) and prints the coral
number of vowels and the total number of consonants in the sentence. The function re-
turns nothing. Note that the sentence could have special characters such as dots, dashes,
and so on.
"""
"""
9. Write a function that takes as input an English sentence (a string) and prints the coral
number of vowels and the total number of consonants in the sentence. The function re-
turns nothing. Note that the sentence could have special characters such as dots, dashes,
and so on.
"""

def stringAnalyse(string):
	cons_count = 0
	vowel_count = 0
	for char in string:
		if char.isalpha():
			char = char.lower()
			if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
				vowel_count = vowel_count + 1
			else:
				cons_count = cons_count + 1
				
	print("Total number of vowels:", vowel_count)
	print("Total number of consonants:", cons_count)

stringAnalyse("Hello, world, and world become better:)")
print()
stringAnalyse("youtube.com is no.1 video streaming platform!")