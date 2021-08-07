# this is an example recursion problem
# classic: given a chessboard of size n, and a starting position of x, y
# can the knight move around the chessboard and touch each square once

import numpy as np 

def get_dimension_input():
    cont_processing = True
    have_received_input = False
    while not have_received_input:
        array_dim_string = input("Please enter array dimension, or q to quit ")
        if array_dim_string.lower() == "q":
            have_received_input = True
            cont_processing = False
            array_dim_int = 0
        else:
            try:
                array_dim_int = int(array_dim_string)
                if array_dim_int <= 0:
                    print("Please enter a positive integer")
                    
                elif array_dim_int % 2 == 0:
                    print("Please enter an odd integer")
                else:
                    have_received_input = True
                    cont_processing = True
            except:
                print("Invalid entry, please try again ")
    return cont_processing, array_dim_int


def create_spiral(my_array, direction, x, y):
    new_direction = direction
    if 0 not in my_array:
        return my_array
    else:
        if direction == "r":
            new_x = x
            new_y = y + 1
            my_array[new_x, new_y] = my_array[x, y] + 1
            if my_array[new_x + 1, new_y] == 0:
                new_direction = "d"
        elif direction == "l":
            new_x = x
            new_y = y  - 1
            my_array[new_x, new_y] = my_array[x, y] + 1
            if my_array[new_x - 1, new_y] == 0:
                new_direction = "u"
        elif direction == "u": 
            new_x = x - 1
            new_y = y
            my_array[new_x, new_y] = my_array[x, y] + 1
            if my_array[new_x, new_y + 1] == 0:
                new_direction = "r"
        else:
            new_x = x + 1
            new_y = y
            my_array[new_x, new_y] = my_array[x, y] + 1
            if my_array[new_x, new_y - 1] == 0:
                new_direction = "l"
        create_spiral(my_array, new_direction, new_x, new_y)
    return my_array


continue_proc, matrix_dim = get_dimension_input()
if continue_proc:
    my_array = np.zeros((matrix_dim, matrix_dim))
    x = matrix_dim // 2
    y = matrix_dim //2
    my_array[x, y] = 1
    go_direction = "r"
    final_array = create_spiral(my_array, go_direction, x, y)
    print(final_array)


