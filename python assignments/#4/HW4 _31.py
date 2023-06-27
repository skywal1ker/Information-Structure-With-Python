
"""
31. Write a program that given a name in the form of ''Chapman, Graham Arthur'' will
convert it to the form ''Graham Arthur Chapman''.
"""
person='Chapman , Graham Arthur'
surname, comma, name, middle=person.split()
full_name = name + ' ' + middle + ' ' + surname
print(full_name)

