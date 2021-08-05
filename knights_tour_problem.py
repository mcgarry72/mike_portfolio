# this is an example recursion problem
# classic: given a chessboard of size n, and a starting position of x, y
# can the knight move around the chessboard and touch each square once

def get_dimension_input():
    cont_processing = True
    have_received_input = False
    while not have_received_input:
        chessboard_dim_string = input("Please enter chessboard dimension, or q to quit ")
        if chessboard_dim_string.lower() == "q":
            have_received_input = True
            cont_processing = False
            chessboard_dim_int = 0
        else:
            try:
                chessboard_dim_int = int(chessboard_dim_string)
                if chessboard_dim_int > 0:
                    have_received_input = True
                else:
                    print("Please enter a positive integer")
            except:
                print("Invalid entry, please try again ")
        return cont_processing, chessboard_dim_int

def get_knight_starting(dim):
    cont_processing = True
    have_received_input = False
    while not have_received_input:
        knight_row_str = input("Please enter the starting row, or q to quit ")
        knight_col_str = input("Please enter the starting column, or q to quit ")
        if knight_row_str.lower() == "q" or knight_col_str.lower() == "q":
            have_received_input = True
            cont_processing = False
            knight_row = 0
            knight_col = 0
        else:
            if not knight_row_str.isdigit() or not knight_col_str.isdigit():
                print("row and column must be integers")
            else:
                knight_row = int(knight_row_str)
                knight_col = int(knight_col_str)
                if knight_row < 1 or knight_col < 1:
                    print("starting positions must be at least one")
                elif knight_row > dim or knight_col > dim:
                    print("starting positions must be less than or equal to the size of the chessboard")
                else:
                    have_received_input = True    
    return cont_processing, knight_row, knight_col

continue_proc, chessboard_dim = get_dimension_input()

if continue_proc:
    continue_proc, start_row, start_col = get_knight_starting(chessboard_dim)
print(continue_proc, chessboard_dim, start_row, start_col)
print("I am done")
