string1 = str(input())
n = int(input())
length = len(string1)
mid = int(length/2)
l1= []
if length%2 == 0:
    string2 = string1[mid-1:]
else:
    string2 = string1[mid:]
for i in range(0,n):
    if i < len(string2):
        l1.append(string2[i])
    else:
        continue
str1 = ''.join(l1)
print(str1)