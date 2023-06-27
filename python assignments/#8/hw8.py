"""
In this assignment you will implement string representation for files. 
you will write editor functions to move the “cursor”. In each representation, you use a cursor to represent the current position. The cursor is just the position (index). Write (and test) the following  10 functions (names are taken from old vi editor) for each implementation
(1)	cmd_h: move cursor one character to the left 
(2)	cmd_I: move cursor one character to the right
(3)	cmd_j: move cursor vertically up one line 
(4)	cmd_k: move cursor vertically down one line
(5)	cmd_X: delete the character to the left of the cursor
(6)	cmd_D: remove on current line from cursor to the end
(7)	cmd_dd: delete current line and move cursor to the beginning of next line
(8)	cmd_ddp: transpose two adjacent lines
(9)	cmd_n:  search for next occurrence of a string (assume that string to be searched is fully in one line.
(10)	cmd_wq: write your representation as text file and save it
Think of and implement any other 10 (interesting!!!) editor commands (your choice)
You can look at some of vi ditor commands for suggestions
"""

txt_str = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated."""



x_list = list(txt_str)
cur_line = 42

# print the separator
def print_file(txt_str, cur_line, sep="^"):                
    print(txt_str[:cur_line] + sep + txt_str[cur_line:] + "\n")


#(1) cmd_h: move cursor one character to the left 
def cmd_h(txt_str, cur_line):                             
    if cur_line > 0:
        cur_line -= 1
    print_file(txt_str, cur_line)
    return txt_str, cur_line



#(2) cmd_I: move cursor one character to the right
def cmd_I(txt_str, cur_line):                              
    if cur_line < len(txt_str):
        cur_line += 1
    print_file(txt_str, cur_line)
    return txt_str, cur_line


#(3) cmd_j: move cursor vertically up one line
def cmd_j(txt_str, cur_line):                          
    up = txt_str.find("\n")
    cur_line = cur_line - up - 2
    print_file(txt_str, cur_line)
    return txt_str, cur_line



#(4) cmd_k: move cursor vertically down one line
def cmd_k(txt_str, cur_line):                             
    up = txt_str.find("\n")
    cur_line = up + cur_line + 2
    print_file(txt_str, cur_line)
    return txt_str, cur_line


 #(5) cmd_X: delete the character to the left of the cursor
def cmd_X(txt_str, cur_line):                             
    if cur_line > 0:
        txt_str = txt_str[ : cur_line - 1] + txt_str[ cur_line : ]
        cur_line -= 1
    print_file(txt_str, cur_line)
    return txt_str, cur_line

#(6) cmd_D: remove on current line from cursor to the end
def cmd_D(txt_str, cur_line):                         
    if cur_line > 0:
        # find the next dot
        dotLoc = txt_str.index(".", cur_line)         
        sub_str = txt_str[cur_line:dotLoc+1]
        txt_str = txt_str.replace(sub_str,"")
        cur_line = cur_line
    print_file(txt_str, cur_line)
    return txt_str, cur_line

#(7) cmd_dd: delete current line and move cursor to the beginning of next line
def cmd_dd(txt_str, cur_line):  
    if cur_line > 0:
        # find the next dot
        dotLoc = txt_str.index(".", cur_line)
        begloc = txt_str.index(".",)
        sub_str2 = txt_str[begloc+1:cur_line]
        sub_str = txt_str[cur_line:dotLoc+1]
        txt_str = txt_str.replace(sub_str,"")
        txt_str = txt_str.replace(sub_str2,"")
        cur_line = cur_line - cur_line
        up = txt_str.find("\n")
        cur_line = up + cur_line + 1
        print_file(txt_str, cur_line)
        return txt_str, cur_line
    return txt_str, cur_line


#(8) cmd_ddp: transpose two adjacent lines
def cmd_ddp()


#(9) cmd_n: search for next occurrence of a string (assume that string to be searched is fully in one line.
def cmd_n(txt_str, cur_line, target):              
    pos = txt_str[cur_line : ].find(target)
    if pos >=0:
        cur_line = cur_line + pos
    print_file(txt_str, cur_line)
    return txt_str, cur_line


#(10) cmd_wq: write your representation as text file and save it
def cmd_wq(y):                              
    out_put = open("out.txt", "w")
    out_put.write(y)
    out_put.close()
    print("Representation to out.txt")
print("Write your representation as text file and then save it:")



# Program of choice

#move to the beginning of the string
def cmd_lb(txt_str, cur_line):                        
    if cur_line < len(txt_str):
        cur_line = 0
    print_file(txt_str, cur_line)
    return txt_str, cur_line

#move to the end of the string
def cmd_le(txt_str, cur_line):                         
    cur_line = len(txt_str)
    print_file(txt_str, cur_line)
    return txt_str, cur_line


#move the cursor to the beginning of the current line
def cmd_strl(y, cur_line): 
    pos = y[:cur_line].rfind("\n")
    if pos != -1:
        cur_line = pos + 1
    else:
        cur_line = 0
    print_file(txt_str, cur_line)
    return y, cur_line


#move the cursor to the end of the current line
def cmd_endl(y, cur_line):                          
    pos = y[cur_line:].find("\n")
    cur_line = cur_line + pos + 1
    print_file(txt_str, cur_line)
    return y, cur_line

#move the cursor to the beginning of the last line
def cmd_lasl(y):                           
    pos = y.rfind("\n")
    cur_line = pos + 1
    print_file(txt_str, cur_line)
    return y, cur_line









print_file(txt_str, cur_line)


#(1) cmd_h:  move cursor one character to the left
x_left, cur_line = cmd_h(txt_str, cur_line)  

#(2) cmd_I:   move cursor one character to the right
x_right, cur_line = cmd_I(txt_str, cur_line) 

#(3) cmd_j: move cursor vertically up one line
x_up, cur_line = cmd_j(txt_str, cur_line)    

#(4) cmd_k: move cursor vertically down one line
x_down, cur_line = cmd_k(txt_str, cur_line)  

#(5) cmd_X: delete the character to the left of the cursor
x_dleft, cur_line = cmd_X(txt_str, cur_line)  


#(6) cmd_D: remove on current line from cursor to the end
x_dright, cur_line = cmd_D(txt_str, cur_line)   

#(7) cmd_dd: delete current line and move cursor to the beginning of next line
x_del, cur_line = cmd_dd(txt_str, cur_line)  

#(8) cmd_ddp: transpose two adjacent lines


#(9) cmd_n: search for next occurrence of a string (assume that string to be searched is fully in one line.
x_nxt, cur_line = cmd_n(txt_str, cur_line, "scar") 


#(10) cmd_wq: write your representation as text file and save it
x_sav, cur_line = cmd_wq(txt_str) 



# program choices

# move to the beginning of the string
x_start, cur_line = cmd_lb(txt_str, cur_line)  

# move to the end of the string
x_end, cur_line = cmd_le(txt_str, cur_line)  

# move the cursor to the beginning of the current line
x_strline, cur_line = cmd_strl(txt_str, cur_line)  

# move the cursor to the end of the current line
x_endline, cur_line = cmd_endl(txt_str, cur_line)  

# move the cursor to the beginning of the last line 
x_lal, cur_line = cmd_lasl(txt_str)  