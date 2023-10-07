#!/usr/bin/env python3

def print_fibonacci(length):

    # Initialize the first two numbers so as to begin logic
    a, b = 0,1
    
    # Initialize an empty list to store the data as we loop
    numbers = []
    
    # create a list using range() and iteration
    for _ in range (length):
        
        numbers.append(a)
        # print(a)
        # print(b) 
        a,b = b, a+b
        # print (a)
    print(numbers,end ='\n')
        
print_fibonacci(2)