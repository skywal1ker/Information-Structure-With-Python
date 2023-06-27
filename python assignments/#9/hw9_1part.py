"""
you will write editor functions to move the “cursor”. In each representation, you use a cursor to represent the current position. The cursor is just the position (index). Write (and test) the following  10 functions (names are taken from old vi editor) for each implementation
(1)	cmd_h:  move cursor one character to the left
(2)	cmd_I:  move cursor one character to the right
(3)	cmd_j: move cursor vertically up one line
(4)	cmd_k: move cursor vertically down one line
(5)	cmd_X: delete the character to the left of the cursor
(6)	cmd_D: remove on current line from cursor to the end
(7)	cmd_dd: delete current line and move cursor to the beginning of next line
(8)	cmd_ddp: transpose two adjacent lines
(9)	cmd_n:   search for next occurrence of a string (assume that string to be searched is fully in one line.
(10)	cmd_wq: write your representation as text file and save it

"""


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

# 1. move cursor one character to the left
def cmd_h(x_list, line, cur):  
    try:
        if cur > 0:
            cur = cur - 1
    except:
        print("Error, try again")
    return x_list, line, cur




# 2. move cursor one character to the left
def cmd_I(x_list, line, cur):  
    try:
        if cur < len(x_list):
            cur = cur + 1
    except:
        print("Error, try again")
    return x_list, line, cur



# 3. move cursor vertically up one line
def cmd_j(x_list, line, cur): 
    try:
        if line == 0:
            cur_line = x_list[line]
            print(cur_line[: cur] + "^" + cur_line[cur:])
            print("\n".join(x_list[line + 1:]) + "\n")
        else:
            print("\n".join(x_list[: line - 1]))
            cur_line = x_list[line - 1]
            print(cur_line[: cur] + "^" + cur_line[cur:])
            print("\n".join(x_list[line:]) + "\n")
    except:
        print("Error, try again")
    return



# 4. move cursor vertically down one line
def cmd_k(x_list, line, cur): 

    try:
        if line == 0:
            print("\n".join(x_list[line: line - 2]))
            cur_line = x_list[line + 1]
            print(cur_line[: cur] + "^" + cur_line[cur:])
            print("\n".join(x_list[line + 2:]) + "\n")
        else:
            print("\n".join(x_list[: line - 1]))
            cur_line = x_list[line - 1]
            print(cur_line[: cur] + "^" + cur_line[cur:])
            print("\n".join(x_list[line :]) + "\n")
    except:
        print("Error, try again")
    return


# 5. Delete the character to the left of the cursor
def cmd_X(x_list, line, cur): 
    try:
        if cur == 0:
            print("\n".join(x_list[: line]))
            cur_line = x_list[line]
            print(cur_line[: cur] + "^" + cur_line[cur:])
            print("\n".join(x_list[line + 1:]) + "\n")
        else:
            print("\n".join(x_list[: line]))
            cur_line = x_list[line]
            print(cur_line[: cur] + "^" + cur_line[cur + 1:])
            print("\n".join(x_list[line + 1 :]) + "\n")
    except:
        print("Error, try again")
    return



# 6. Remove on current line from cursor to the end
def cmd_D(x_list, line, cur):  
    try:
        x_list[line] = x_list[line][: cur]
        return x_list, line, cur
    except:
        print("Error, try again")



# 7. Delete current line and move cursor to the beginning of next line
def cmd_dd(x_list, line, cur):  
    try:
        if line < len(x_list) - 1:
            x_list.pop(line)
            cur = 0
            return x_list, line, cur
    except:
        print("Error, try again")



# 8. Transpose two adjacent lines
def cmd_ddp(x_list, line, cur):  
    try:
        if line > 0:
            x_list[line - 1], x_list[line] = x_list[line], x_list[line - 1]
            line = line - 1
            return x_list, line, cur
    except:
        print("Error, try again")



# 9. Search for next occurrence of a string
def cmd_n(x_list, line, cur, target):  
    try:
        for line_id in range(line, len(x_list)):
            next_line = x_list[line_id]
            pos = next_line.find(target)
            if pos >= 0:
                return x_list, line_id, pos
        return x_list, line, cur
    except:
        print("Error, try again")

# 10 
def cmd_wq(x_str):
    with open('reports.txt', 'w') as e:
        e.writelines("%s\n" % x_str)



print_file(x_list, line, cur)
x_list, line, cur = cmd_h(x_list, line, cur)
print_file(x_list, line, cur)
x_list, line, cur = cmd_I(x_list, line, cur)

print_file(x_list, line, cur)
cmd_j(x_list, line, cur)
cmd_k(x_list, line, cur)
cmd_X(x_list, line, cur)

x_list, line, cur = cmd_D(x_list, line, cur)
print_file(x_list, line, cur)

x_list, line, cur = cmd_dd(x_list, line, cur)
print_file(x_list, line, cur)

x_list, line, cur = cmd_ddp(x_list, line, cur)
print_file(x_list, line, cur)

x_list, line, cur = cmd_n(x_list, line, cur, "es")
print_file(x_list, line, cur)

cmd_wq(x_str)