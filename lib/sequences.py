#!/usr/bin/env python3

def print_fibonacci(length):

    # Initialize the first two numbers so as to begin logic
    a, b = 0,1
    
    # Initialize an empty list to store the data as we loop
    numbers = []
    
    # create a list using range() and iteration
    for nums in range (length):
        
        numbers.append(a)
        print(numbers)
        a,b = b, a+b
        print(numbers)
        
print(print_fibonacci(10))