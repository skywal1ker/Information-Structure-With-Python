x_str = """Today
is a new
Wedenesday"""

x_list = x_str.split("\n")

line = 1
cur = 3


def print_file(x_list, line, cur):
    print("\n".join(x_list[: line]))
    cur_line = x_list[line]
    print(cur_line[: cur] + "^" + cur_line[cur:])
    print("\n".join(x_list[line + 1:]) + "\n")
    return

# 1. Remove from the right
def cmd_1(x_list, line, cur):  
    try:
        x_list[line] = x_list[line][:cur]
        return x_list, line, cur
    except:
        print("Error, try again")
        
# 2. Remove first letter
def cmd_2(x_list, line, cur):  
    try:
        x_list[line] = x_list[line][-2:cur]
        return x_list, line, cur
    except:
        print("Error, try again")

 
# 3. Remove all letters but not deleting current line
def cmd_3(x_list, line, cur):  
    try:
        x_list[line] = x_list[line][cur:-1]
        return x_list, line, cur
    except:
        print("Error, try again")       


# 4. moving to the first line on the after third letter
def cmd_4(x_list, line, cur):  
    try:
        if line > 0:
            x_list[line]
            line = line - 1 
            return x_list, line, cur
    except:
        print("Error, try again")

# 5. copying 3 letters from next word
def cmd_5(x_list, line, cur):  
    try:
        x_list[line] = x_list[-1][: cur]
        return x_list, line, cur
    except:
        print("Error, try again")   

# 6. move the cursor to the beginning of the current line
def cmd_6(x_list, line, cur):  
    try:
        if cur > 0:
            cur = 0
        return x_list, line, cur
    except:
        print("some error in code")


#7. move cursor to the end of the current line
def cmd_7(x_list, line, cur): 
    try:
        if cur < len(x_str):
            cur = len(x_str)
        return x_list, line, cur
    except:
        print("some error in code")

print_file(x_list, line, cur)
x_list, line, cur = cmd_1(x_list, line, cur)
print_file(x_list, line, cur)

x_list, line, cur = cmd_2(x_list, line, cur)
print_file(x_list, line, cur)

x_list, line, cur = cmd_3(x_list, line, cur)
print_file(x_list, line, cur)

x_list, line, cur = cmd_4(x_list, line, cur)
print_file(x_list, line, cur)

x_list, line, cur = cmd_5(x_list, line, cur)
print_file(x_list, line, cur)

x_list, line, cur = cmd_6(x_list, line, cur)
print_file(x_list, line, cur)

x_list, line, cur = cmd_7(x_list, line, cur)
print_file(x_list, line, cur)