import string
def print_rangoli(size):
    # alphabet = string.ascii_lowercase
    # pattern = alphabet[:size]
    # m = 2*n-1
    # n = 2*size - 1
    #  for j in range(0,size):
    #      c=alphabet[j]
    
    
    # for i in range(0,n//2):
    #     r_part = pattern[len(pattern)-i:]
    #     l_part = r_part[:-1][:i-1]
    #     all_part = l_part+r_part
    #     joining = "-".join(all_part)
    #     final = joining.center(m,"-") 
    #     print(final)           
    # print('-'.join(pattern[::-1]+pattern[1:]))
    # for j in range(n//2,0,-1):
    #     r_part1 = pattern[len(pattern)-j]
    #     l_part1 = r_part1[::-1][:j-1]
    #     all_partl=l_part1+r_part1
    #     joining1= "-".join(all_partl)
    #     final1= joining1.center(m,"-")
    #     print(final1)
        # considering size = 5
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    pattern = alphabet[:size] # if size = 5 ; then 'abcde'
    
    
    row_length = size * 2 - 1 # 9 rows/lines in total
    col_length = 2 * row_length - 1  # 17 characters per row
    size_until_mid = (row_length-1)//2
    
    down = []
    
    # top               beginning to mid
    for i in range(1, size_until_mid + 1):
        r_part = pattern[len(pattern) - i:]  # bcde
        l_part = r_part[::-1] [:i-1]         # edc
        all_part = l_part + r_part    # edc + bcde = edcbcde
        joining = "-".join(all_part)         #e-d-c-b-c-d-e
        final = joining.center(col_length,'-') # putting dashes 
        down.append(final)     # adding to list (for bottom part)
        print(final)
    
    # middle
    print("-".join(pattern[::-1]+pattern[1:]))
    
    # down           mid to down (same length as begin to mid)   
    for _ in range(size_until_mid):
        print(down.pop()) # .pop > first in last out (FIFO)
        # thus, no need to reverse it    
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)