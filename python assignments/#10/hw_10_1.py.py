"""
you will write editor functions to move the “cursor”. In each representation, you use a cursor to represent the current position. The cursor is just the position (index). Write (and test) the following  10 functions (names are taken from old vi editor) for each implementation
(1)	cmd_h:  move cursor one character to the left
(2)	cmd_I:   move cursor one character to the right
(3)	cmd_j: move cursor vertically up one line
(4)	cmd_k: move cursor vertically down one line
(5)	cmd_X: delete the character to the left of the cursor
(6)	cmd_D: remove on current line from cursor to the end
(7)	cmd_dd: delete current line and move cursor to the beginning of next line
(8)	cmd_ddp: transpose two adjacent lines
(9)	cmd_n:   search for next occurrence of a string (assume that string to be searched is fully in one line.
(10)	cmd_wq: write your representation as text file and save it
Think of and implement any other 10 (interesting!!!) editor commands (your choice)
"""
# double linked list editor

NEXT_PTR, PREV_PTR = 1, 2

x_str = """Today
is a new
Wednesday"""

k = x_str
k_list = k.strip("/n")




def get_linked_list(y):  # y is a string
    y_list = y.split("\n")
    head, tail = None, None
    for next_line in y_list:
        next_node = [next_line, None, None]
        if head is None:
            head = next_node
            tail = next_node
        else:
            next_node[PREV_PTR] = tail
            tail[NEXT_PTR] = next_node
            tail = next_node
    return head, tail


def print_double_list(head, tail):
    cur_node = head
    while cur_node is not None:
        print(cur_node[0])
        cur_node = cur_node[NEXT_PTR]
    return


def print_file_double_list(head, tail, cursor_node, cursor):
    next_node = head
    while next_node is not None:
        if next_node is cursor_node:
            c_line = next_node[0]
            print(c_line[: cursor] + "$" + c_line[cursor:])
        else:
            print(next_node[0])
        next_node = next_node[NEXT_PTR]
    print("--------")
    return

 # 1. move left one
def cmd_h(head, tail, cursor_node, cursor): 
    if cursor > 0:
        cursor = cursor - 1
    return head, tail, cursor_node, cursor

# 2. move right one
def cmd_I(head, tail, cursor_node, cursor):  
    if cursor < len(k_list):
        cursor = cursor + 1
    return head, tail, cursor_node, cursor

#3. move cursor vertically up one line
def cmd_j(head, tail, cursor_node, cursor):  
    if cursor_node[PREV_PTR] is not None:
        cursor_node = cursor_node[PREV_PTR]
        new_line = cursor_node[0]
        if len(new_line) < cursor:
            cursor = len(new_line)
    return head, tail, cursor_node, cursor

#4. move cursor vertically down one line
def cmd_k(head, tail, cursor_node, cursor):  
    if cursor_node[NEXT_PTR] is not None:
        cursor_node = cursor_node[NEXT_PTR]
        new_line = cursor_node[0]
        if len(new_line) < cursor:
            cursor = len(new_line)
    return head, tail, cursor_node, cursor


# 5. delete to the left
def cmd_X(head, tail, cursor_node, cursor):  
    if cursor_node is not None:
        c_line = cursor_node[0]
        new_line = c_line[: cursor - 2] + c_line[cursor:]
        if cursor < len(cursor_node[0]):
            cursor = cursor - 2
        cursor_node[0] = new_line
    return head, tail, cursor_node, cursor

# 6. remove rest of line to the right
def cmd_D(head, tail, cursor_node, cursor):  
    if cursor_node is not None:
        c_line = cursor_node[0]
        new_line = c_line[: cursor]
        cursor_node[0] = new_line
    return head, tail, cursor_node, cursor


#7. delete current line and move cursor to the beginning of next line
def cmd_dd(head, tail, cursor_node, cursor):  
    previous_node = cursor_node[PREV_PTR]
    if cursor_node[NEXT_PTR] is not None:
        previous_node[NEXT_PTR] = cursor_node[NEXT_PTR]
        cursor = 0
    return head, tail, previous_node[NEXT_PTR], cursor



#8. transpose two adjacent lines
def cmd_ddp(head, tail, cursor_node, cursor):  
    if cursor_node is not head:
        prev_node = cursor_node[PREV_PTR]
        t = [None, None, None, None]
        t[0] = prev_node[0]
        t[NEXT_PTR] = cursor_node[NEXT_PTR]
        t[PREV_PTR] = cursor_node
        if (prev_node[PREV_PTR] != None):
            cursor_node[PREV_PTR] = prev_node[PREV_PTR]
    cursor_node[NEXT_PTR] = t
    head = cursor_node
    return head, tail, t, cursor


#9. search for string(not completed)
def cmd_n(head, tail, cursor_node, cursor, target):
    return head, tail, cursor_node, cursor

# 10 write your representation as text file and save it
def cmd_wq(head):  
    current_node = head
    out_file = open("output.txt", "w")
    while current_node is not None:
        out_file.write(current_node[0] + "\n")
        current_node = current_node[NEXT_PTR]
    out_file.close()
    print("File saved to output.txt")
    return head



head, tail = get_linked_list(x_str)

cursor_node, cursor = head[NEXT_PTR], 5
print_file_double_list(head, tail, cursor_node, cursor)

head, tail, cursor_node, cursor = cmd_h(head, tail, cursor_node, cursor)
print_file_double_list(head, tail, cursor_node, cursor)

head, tail, cursor_node, cursor = cmd_I(head, tail, cursor_node, cursor)
print_file_double_list(head, tail, cursor_node, cursor)

head, tail, cursor_node, cursor = cmd_j(head, tail, cursor_node, cursor)
print_file_double_list(head, tail, cursor_node, cursor)

head, tail, cursor_node, cursor = cmd_k(head, tail, cursor_node, cursor)
print_file_double_list(head, tail, cursor_node, cursor)

head, tail, cursor_node, cursor = cmd_X(head, tail, cursor_node, cursor)
print_file_double_list(head, tail, cursor_node, cursor)

head, tail, cursor_node, cursor = cmd_D(head, tail, cursor_node, cursor)
print_file_double_list(head, tail, cursor_node, cursor)

head, tail, cursor_node, cursor = cmd_dd(head, tail, cursor_node, cursor)
print_file_double_list(head, tail, cursor_node, cursor)

head, tail, cursor_node, cursor = cmd_ddp(head, tail, cursor_node, cursor)
print_file_double_list(head, tail, cursor_node, cursor)

head = cmd_wq(head)