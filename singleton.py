# program that receives input, an array of integers
# one of the integers is a singleton
# the program returns the singleton
# if no singleton, return null

array_list = []
continue_input = True
while continue_input:
    in_value = input("Please enter an integer, or q to quit ")
    if in_value.lower() == 'q': 
        continue_input = False
    else:
        try:
            array_list.append(int(in_value))
        except:
            print(f"{in_value} is not an integer")

found_a_singleton = False
if len(array_list) == 0:
    print("No items entered")
elif len(array_list) == 1:
    print(f"Singleton is {array_list[0]}")
    found_a_singleton = True
else:
    for x in array_list:
        if array_list.count(x) == 1:
            print(f"{x} is a singleton!")
            found_a_singleton = True

if not found_a_singleton:    
    print("There are no singletons!")
print("done")