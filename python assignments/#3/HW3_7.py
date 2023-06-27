"""20. Write a program that prompts for an integer and prints the integer, but if something
other than an integer is input, the program keeps asking for an integer. Here is a sample
session:
Input an integer: abc
Error: try again. Input an integer: 4a
Error: try again. Input an integer: 2.5
Error: try again. Input an integer: 123
The integer is: 123
Hint: The string isdigit method will be useful."""


try:
  input_value = input("Please enter the integer: ")
  int_value = int(input_value)
  print("The integer is: ",int_value)
except:
    str_value = str(input_value)
    print("Error: try again. Input an integer: ", str_value)
 
 