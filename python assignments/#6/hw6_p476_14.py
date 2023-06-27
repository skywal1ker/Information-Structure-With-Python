"""
14. Letter Counts Using Dictionaries
Remember to consider spaces as a special case.
(a) Write a function that takes as input a string and returns the most common letter in
the string.
(b) Write a function that takes as input a string and returns a dictionary of letter counts.
(c) Write a function that takes as input a string and prints a histogram of letter counts,
A histogram can be done with matplotlib or using different length strings of characters.
"""


# (a) Write a function that takes as input a string and returns the most common letter in

def most_common_letter():
    str_input = str(input("Please enter the str words for (a) task: "))
    letters = set(str_input)
    if " " in letters:
        letters.remove(" ")
    max_count = 0
    freq_letter = []
    for letter in letters:
        count = 0
        for char in str_input:
            if char == letter:
                count += 1
        if count == max_count:
            max_count = count
            freq_letter.append(letter)
        if count > max_count:
            max_count = count
            freq_letter.clear()
            freq_letter.append(letter)
    print("The most frequent letter is ", freq_letter, ":", max_count, "times")


most_common_letter()


# (b) Write a function that takes as input a string and returns a dictionary of letter counts.
def count_char():
    str_input = str(input("Please enter the str words for (b) task: "))
    dict1 = {}
    count = 0
    for i in str_input:
        if i in dict1.keys():
            dict1[i] += 1
        else:
            dict1[i] = 1
    for j in dict1.values():
        count += j
    print(dict1)
    print(count)


count_char()


# (c) Write a function that takes as input a string and prints a histogram of letter counts,
def print_as_histogram():
    list_of_sentences = str(input("Input the text for a histogram counts, please: "))
    m_dict = {}
    for sentence in list_of_sentences:
        for letter in sentence:
            if letter.isalpha():
                if letter in m_dict.keys():
                    m_dict[letter] += 1
                else:
                    m_dict[letter] = 1
    for letter in sorted(m_dict.keys()):
        print(f'{letter} | {"*" * m_dict[letter]}')


print_as_histogram()
