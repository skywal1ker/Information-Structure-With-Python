NEXT_PTR, PREV_PTR = 1, 2

x_str = """Today
is a new
Wednesday"""

k = x_str
x_list = k.strip("/n")


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


# 8.move cursor to the beginning of the current line and delete everything before the cursor 
def cmd_8(head, tail, cursor_node, cursor):  
    if cursor_node is not None:
        c_line = cursor_node[0]
        new_line = c_line[cursor:]
        cursor_node[0] = new_line
        c_line = cursor_node[0]
        new_line = c_line[: cursor] + c_line[cursor :]
        cursor = 0
        cursor_node[0] = new_line
    return head, tail, cursor_node, cursor







head, tail = get_linked_list(x_str)

cursor_node, cursor = head[NEXT_PTR], 5
print_file_double_list(head, tail, cursor_node, cursor)

head, tail, cursor_node, cursor = cmd_8(head, tail, cursor_node, cursor)
print_file_double_list(head, tail, cursor_node, cursor)


