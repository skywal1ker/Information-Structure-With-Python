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


# 1. Add character after the cursor
def cmd_1(head, tail, cursor_node, cursor):  
    if cursor_node is not None:
        c_line = cursor_node[0]
        new_line = c_line[: cursor] + "%" + c_line[cursor - 1:]
        if cursor < len(cursor_node[0]):
            cursor = cursor
        cursor_node[0] = new_line
    return head, tail, cursor_node, cursor


# 2. Add character before the cursor
def cmd_2(head, tail, cursor_node, cursor):  
    if cursor_node is not None:
        c_line = cursor_node[0]
        new_line = c_line[: cursor] + c_line[cursor:]
        if cursor < len(cursor_node[0]):
            cursor = cursor + 1
        cursor_node[0] = new_line
    return head, tail, cursor_node, cursor

# 3. move the cursor to the beginning of the current line
def cmd_3(head, tail, cursor_node, cursor):  
    if cursor_node is not None:
        c_line = cursor_node[0]
        new_line = c_line[: cursor] + c_line[cursor :]
        if cursor < len(cursor_node[0]):
            cursor = 0
        cursor_node[0] = new_line
    return head, tail, cursor_node, cursor


# 4. move the cursor to the end of the current line
def cmd_4(head, tail, cursor_node, cursor):  
    if cursor_node is not None:
        c_line = cursor_node[0]
        new_line = c_line[: cursor] + c_line[cursor :]
        if cursor < len(cursor_node[0]):
            cursor = len(cursor_node[0])
        cursor_node[0] = new_line
    return head, tail, cursor_node, cursor


#5. move cursor to the beginning of the list
def cmd_5(head, tail, cursor_node, cursor):  
        if cursor_node is not None:
            c_line = cursor_node[0]
            new_line = c_line[: cursor] + c_line[cursor :]
            if cursor < len(cursor_node[0]):
                cursor = 0
        cursor_node[0] = new_line
        if cursor_node[PREV_PTR] is not None:
            cursor_node = cursor_node[PREV_PTR]
            new_line = cursor_node[0]
            if len(new_line) < cursor:
                cursor = len(new_line)
        return head, tail, cursor_node, cursor




head, tail = get_linked_list(x_str)


cursor_node, cursor = head[NEXT_PTR], 5

print_file_double_list(head, tail, cursor_node, cursor)

head, tail, cursor_node, cursor = cmd_1(head, tail, cursor_node, cursor)
print_file_double_list(head, tail, cursor_node, cursor)

head, tail, cursor_node, cursor = cmd_2(head, tail, cursor_node, cursor)
print_file_double_list(head, tail, cursor_node, cursor)

head, tail, cursor_node, cursor = cmd_3(head, tail, cursor_node, cursor)
print_file_double_list(head, tail, cursor_node, cursor)

head, tail, cursor_node, cursor = cmd_4(head, tail, cursor_node, cursor)
print_file_double_list(head, tail, cursor_node, cursor)

head, tail, cursor_node, cursor = cmd_5(head, tail, cursor_node, cursor)
print_file_double_list(head, tail, cursor_node, cursor)
