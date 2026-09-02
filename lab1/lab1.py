# Dimitri Cognata

# Course: Comp 590

# Lab: Lab 1

# Fib sequence taken from GeekforGeeks

# https://www.geeksforgeeks.org/python/python-program-to-print-the-fibonacci-sequence/

def fibonacci(n):
    # Return the base Fib numbers

    if n <= 1:
        return n

    #Calculate the number using the previous two numbers
    return fibonacci(n -1) + fibonacci(n -2)


# Write the first 25 fib numbers to an ouput file
with open("output/fibonacci.txt", "w") as file:
    for number in range(25):
        print(fibonacci(number), file=file)

