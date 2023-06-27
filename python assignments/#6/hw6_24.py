"""
24. Make a list of the words in a sentence. No punctuation should be attached to a "word"
in your list, for example, "end." is not a correct word, but "end" is.
(a) Use a while loop.
(b) Use a for loop.
"""

import string

def create_list_of_words(sentence):
    sentence_list = sentence.split()
    list_of_words = []

    for word in sentence_list:
        list_of_words.append(word.strip(string.punctuation))
    print("(b) For loop:", list_of_words)


create_list_of_words("Another way to die")

def create_list_of_words_while(sentence):
    sentence_list = sentence.split()
    list_of_words = []

    while sentence_list:
        word = sentence_list.pop(0)
        list_of_words.append(word.strip(string.punctuation))

    print("(a) While loop: ", list_of_words)


create_list_of_words_while("let me down easy")