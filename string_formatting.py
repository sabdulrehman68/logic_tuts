

def print_formatted(number):
    num = bin(number)
    m = len(num)-1
    
    for i in range(1,number+1):
        hexa = str(hex(i)).replace("0x","")
        octa = oct(i).replace("0o","")
        binary = bin(i).replace("0b","")
        if hexa.isalpha():
            hexa = hexa.upper()
        
        if hexa.isalnum():
            if len(hexa)==2:
                if hexa[1].isalpha():
                    he = hexa.split()
                    # print(len(he))
                    he[0]=he[0].upper()
                    hexa = ""
                    hexa = hexa.join(he)        
        print(str(i).rjust(m-1)+(str(octa)).rjust(m)+(str(hexa)).rjust(m)+(str(binary)).rjust(m))
        # print(f" {binary}")
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)