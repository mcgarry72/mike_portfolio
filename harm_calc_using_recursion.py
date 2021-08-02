# program which uses recrsion to calculate the harmonic sum

import sys

def calc_harm_sum(n):
    if n == 1:
        return(1)
    elif n < 1:
        return(None)
    else:
        return(1 / n + calc_harm_sum(n-1))


max_number = sys.getrecursionlimit()

cont_input = True
while cont_input:
    user_input = input("Please enter a positive integer ")
    print(user_input)
    calc_int = int(user_input)
    print(calc_int)
    if calc_int < 0:
        print("invalid entry - input must be a positive number")
    elif calc_int == 0:
        print("input cannot be zero")
    elif calc_int >= max_number:
        print(f"Input error - number cannot be greater than or equal to {max_number}")
    else:
        print("The harmonic sequence of " + user_input + " is " + str(calc_harm_sum(calc_int)))
        cont_input = False

print("Finished processing")