def searchMyString(strings_list,target):
    index = 0
    for i in range(0,len(strings_list)):
        element = strings_list[i]
        if element == target:
            index = i
            break
    return index

no = int(input())
str_list = []
for i in range(0,no):
    ele = str(input())
    str_list.append(ele)

search = str(input())
index = searchMyString(str_list,search)

print(f"Position of the searched string is:{index}")