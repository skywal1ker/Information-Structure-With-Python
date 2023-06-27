"""
11. Write a function named safe_ input (prompt, type) that works like the Python input
function, except that it only accepts the specified type of input. The function takes
two arguments:
• prompt: str
• type: int, float, str
The function will keep prompting for input until correct input of the specified
type is entered.
The function returns the input. If the input was specified to be a number (float
or int), the value returned will be of the correct type; that is, the function will perform
the conversion.
The default for a prompt is the empty string. The default for the type is string.
"""

def safe_input(prompt="", type="string"):
   try:
       if type == "float":
           val = float(input(prompt))
       elif type == "int":
           val = int(input(prompt))
       elif type == "string":
           val = input(prompt)
       else:
           print("Invalid input, try again. ")
           val = 0
       return val
   except ValueError:
       return safe_input(prompt, type)


print("Enter the prompt: ")
prompt = input()

print("Enter the type i.e float, int or string: ")
type = input()

print(prompt)
result = safe_input(prompt,type)

print(result)
