num = int(input("Enter no. of keys:"))
dict1 = {}
for i in range(0,num):
    key = input("Enter key:")
    value = input("Enter value:")
    dict1[key] = value


def key_val_swapper(dictionary):
    dict2 = {}
    for key,values in dictionary.items():
        dict2[values] = key

    return dict2

d = key_val_swapper(dict1)
print(dict1)
print(d)
