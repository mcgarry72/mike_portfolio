import re

# program which validates a postal code
# a valid post code is between 10000 and 99999
# and does not have more than 1 alternative repeating digit

def check_zip_code_function(input_string):
    non_recurring_count = 0
    for counter in range(len(input_string) - 2):
        if input_string[counter] == input_string[counter + 2]:
            non_recurring_count += 1
    if non_recurring_count < 2:
        return(True)
    else:    
        return(False)


no_input = True
while no_input:
    zip_code_to_be_checked = input(f"Please enter a 5 digit integer, between 100000 and 99999, or q to quit ")
    if zip_code_to_be_checked.lower() == 'q':
        no_input = False
    else:
        if len(zip_code_to_be_checked) != 5:
            print("Input must be 5 digits!")
        else:
            try:
                int_zip_code = int(zip_code_to_be_checked)
                if int_zip_code >= 10000 and int_zip_code <= 99999:
                    result = check_zip_code_function(zip_code_to_be_checked)
                    if result:
                        print(f"{zip_code_to_be_checked} is valid!")
                    else:
                        print(f"{zip_code_to_be_checked} is not valid!")
                else:
                    print("Input must be between 10000 and 9999")
            except:
                print("Invalid input - must be all numbers")
print("I am done")