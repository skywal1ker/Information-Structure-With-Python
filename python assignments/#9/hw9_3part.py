x_str = """Today
is a new
Wednesday"""


x_list = x_str.split("\n")

line = 1
cur = 2


def print_file(x_list, line, cur):
    print("\n".join(x_list[: line]))
    cur_line = x_list[line]
    print(cur_line[: cur] + "^" + cur_line[cur:])
    print("\n".join(x_list[line + 1:]) + "\n")
    return


# my own choices
# 8. add three character before the cursor
def cmd_8(x_list, line, cur):  
    try:
        if cur < len(x_list):
            cur = cur + 1
            print("\n".join(x_list[: line]))
            cur_line = x_list[line]
            print(cur_line[: cur] + "$$$" + "^" + cur_line[cur:])
            print("\n".join(x_list[line + 1:]) + "\n")
        return x_list, line, cur
    except:
        print("error in code")


 #9 . add a character after the cursor
def cmd_9(x_list, line, cur): 
    try:
        if cur <= len(x_list):
            cur = cur + 1
            print("\n".join(x_list[: line]))
            cur_line = x_list[line]
            print(cur_line[: cur] + "^" + "$$$" + cur_line[cur:])
            print("\n".join(x_list[line + 1:]) + "\n")
        return x_list, line, cur
    except:
        print("error in code")

 # 10. delete everything before the cursor and move cursor to the beginning
def cmd_10(x_list, line, cur):
    try:
        x_list[line] = x_list[line][cur:]
        cur = 0
        return x_list, line, cur
    except:
        print("Error, try again")




print_file(x_list, line, cur)

x_list, line, cur = cmd_8(x_list, line, cur)
x_list, line, cur = cmd_9(x_list, line, cur)



print_file(x_list, line, cur)
x_list, line, cur = cmd_10(x_list, line, cur)
print_file(x_list, line, cur)