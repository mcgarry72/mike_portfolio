# program to get the nth fibonacci number

def fibonacci(input_integer):
    if input_integer == 1 or input_integer == 2:
        return(1)
    else:
        return(fibonacci(input_integer - 1) + fibonacci(input_integer -2))
    
print(fibonacci(1))
print("done")
