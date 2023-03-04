def isValid(list):
    count1 = 0
    count2 = 0
    for str1 in list:
        if str1.isalpha():
            count1 += 1
        else:
            count2 += 1

    print("Count Of Valid Strings="+str(count1))
    print("Count Of Invalid Strings="+str(count2))

elements = int(input())
i = 0
l1 = []
for i in range(0,elements):
    str1 = str(input())
    l1.append(str1)

isValid(l1)
# print(l1)
