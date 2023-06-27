"""
12. Write a function named prompt_open that prompts for a file name and repeatedly
attempts to read the specified file until a correctly specified file has been entered. The
function takes one mode argument, *r' or 'w' and returns the file handle that open
returns.
"""


def prompt_open():
    while True:
        file_name = input("Enter a file name: ")
        try:
            x_file = open(file_name,'r')
            return x_file
        except FileNotFoundError:
            print("File not found")
            pass
open_file = prompt_open()
print(open_file)

