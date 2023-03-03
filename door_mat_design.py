n , m = input().split(" ")
n = int(n)
m= int(m)
c = ".|."
d= "WELCOME"
j=1
if n%2 !=0 and n>=1:
    for i in range(0,int(n/2)):
        print((c*(i+j)).center(m,"-"))
        j+=1
    print(d.center(m,"-"))
    for k in range(int(n/2),0,-1):
        print((c*(k*2-1)).center(m,"-"))
    # if i in range(n//2+2,n+1):
    #     print((c*(i-j)).center(m,"-"))
    #     j=j+3

    