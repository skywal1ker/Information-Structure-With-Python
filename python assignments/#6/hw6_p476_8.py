"""
8. If my_dict = {'a': 15, 'c' :35, 'b' :20}, write Python code
(a) to print all the keys.
(b) to print all the values.
(c) to print all the keys and values pairs.
(d) to print all the keys and values pairs in order of key.
(e) to print all the keys and values pairs in order of value.
"""
dct = {'a': 15, 'c': 35, 'b': 20}
keys_dict = dct.keys()
val_dict = dct.values()

# (a)
print("Print all the keys: ", keys_dict)

# (b)
print("Print all the values: ", val_dict)

# (c)
print("Print all the keys and values pairs: ", dct)

# d)
print("Print all the keys and values pairs in order of value: ", )
orders = {
    'b': 35,
    'c': 20,
    'a': 15,
}
sort_orders = sorted(orders.items(), key=lambda x: x[1])
for i in sort_orders:
    print(i[1])

# e
print("Print all the keys and values pairs in order of key: ", )
orders = {
    'b': 35,
    'c': 20,
    'a': 15,
}
sort_orders = sorted(orders.items(), key=lambda x: x[0])
for i in sort_orders:
    print(i[0])
