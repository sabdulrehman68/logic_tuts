def isPalindrome(string1):
    stringi = string1[::-1]
    if string1 == stringi:
        return True
    else:
        return False

def new_pal(striing):
    l =[]
    length = len(striing)
    l.append(striing[1])
    l.append(striing[1:length-1])
    l.append(striing[length-1])
    return l
def get_palindrome(string,l1):
    
    if len(string)>=1:
        for i in range(2,len(string)+1):
            str1 = string[0:i]
            
            if isPalindrome(str1) == True:
                l1.append(str1)
                str2 = string[i:]
                get_palindrome(str2,l1)
                
            else:
                continue
    if len(l1)==3:    
        return l1 
    else:
        return "impossible"
        

l1=[]
string = str(input())
if isPalindrome(string):
    l = new_pal(string)
else:
    l = get_palindrome(string,l1)
for j in range(0,len(l)):
    print(l[j])