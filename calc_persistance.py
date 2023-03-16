def additive_persistance(number,numbers):
    num = str(number)
    sum = 0
    
    for i in range(0,len(num)):
        sum = sum + int(num[i])
    
    numbers.append(sum)
    if len(str(sum)) == 1:
        count = len(numbers)
        return count
        
    else:
        num1 = sum
        return additive_persistance(num1,numbers)

def multiplicative_persistance(number,numbers):
    num = str(number)
    pro = 1
    
    for j in range(0,len(num)):
        pro = pro * int(num[j])

    numbers.append(pro)
    if len(str(pro)) == 1 :
        count = len(numbers)
        return count
        
    else:
        num1 = pro
        return multiplicative_persistance(num1,numbers)

numa = []
numb = []
inp = int(input())
if inp > 9:
    sum = additive_persistance(inp,numa)
    pro = multiplicative_persistance(inp,numb)
    print(sum)
    print(pro)
else:
    print("Enter No. greater than 9")