"""
30. Using the find method, write a short program that will print out the index of both 'o's
when given the input “Who's on first?”.
"""
str_txt = "Who's on first?"
find_letter = "o"
lst_emp = []
for pos,char in enumerate(str_txt):
    if(char == find_letter):
        lst_emp.append(pos)
print(lst_emp)
