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

#10. Keeping the current line
def cmd_10(head, tail, cursor_node, cursor):  
    if cursor_node is not head:
        prev_node = cursor_node[PREV_PTR]
        t = [None, None, None, None]
        t[0] = prev_node[0]
        t[NEXT_PTR] = cursor_node[NEXT_PTR]
        t[PREV_PTR] = cursor_node[NEXT_PTR]
        if (prev_node[PREV_PTR] != None):
            cursor_node[PREV_PTR] = prev_node[PREV_PTR]
            cursor_node[NEXT_PTR] = prev_node[PREV_PTR]
    cursor_node[PREV_PTR] = head
    t = head # cursor at the start
    head = cursor_node
    t = head
    tail = head
    cursor_node[PREV_PTR] = head
    t = head # cursor at the start
    head = cursor_node
    cursor_node[PREV_PTR] = prev_node[PREV_PTR]
    cursor_node[NEXT_PTR] = head[PREV_PTR]
    t = head
    tail = head


    return head, tail, t, cursor




head, tail = get_linked_list(x_str)

cursor_node, cursor = head[NEXT_PTR], 5
print_file_double_list(head, tail, cursor_node, cursor)

head, tail, cursor_node, cursor = cmd_10(head, tail, cursor_node, cursor)
print_file_double_list(head, tail, cursor_node, cursor)