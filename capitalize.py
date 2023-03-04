#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    lst = s.split(" ")
    f_name = lst[0]
    
    l_name = lst[1]
    l1 = list(f_name)
    print(l1[0])
    l1[0] = l1[0].upper()
    print(l1[0])
    # print(l1)
    f_name = ""
    f_name= f_name.join(str(x) for x in l1)
    l2 = list(l_name)
    l2[0]=l2[0].upper()
    l_name = ""
    l_name = l_name.join(l2)
    lst[0] = f_name
    lst[1] = l_name 
    # for i in range(0,len(lst)):
    #     l1 = lst[i].split()
    #     l1[0]=l1[0].upper()
    #     st = "".join(l1)
    #     lst[i]=st

    s = " ".join(lst)
    print(s)

    # return " ".join(list(map(str.capitalize, s.split(" "))))

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    # fptr.write(result + '\n')

    # fptr.close()
