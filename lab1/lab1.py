# Dimitri Cognata

# Course: COMP 590

# Lab: Lab 1

# Fib sequence logic taken from GeekforGeeks:

# https://www.geeksforgeeks.org/python/python-program-to-print-the-fibonacci-sequence/

def fibonacci(n):
    # start with the first two fib numbers
    a, b = 0, 1

    #write the first numbers to the output file
    with open("output/fibonacci.txt","w") as file:
        for _ in range(n):
            print(a, file=file)
            a, b = b, a + b

#generat the first 25 fib numbers
fibonacci(25)
