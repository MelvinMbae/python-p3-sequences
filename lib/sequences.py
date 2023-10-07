#!/usr/bin/env python3

def print_fibonacci(length):

    n1, n2 = 0,1
    count = 0
    
    
    while count < length:
        print(n1)
        nth = n1+n2
        n1 = n2
        n2 = nth
        count +=1
        
print(print_fibonacci(10))