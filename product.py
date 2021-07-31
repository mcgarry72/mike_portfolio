# program to determine if 
# an integer is the product of any other two elements in an array
# for example, the list [4, 4, 16, 19] would return 16 (product of 4 x 4)

def find_product(array_list):
    product_value = False
    value = None
    i = 0
    while i < len(array_list) and not product_value:
        j = i + 1
        while j < len(array_list) and not product_value:
            calc_value = array_list[i] * array_list[j]
            if calc_value in array_list:
                product_value = True
                value = calc_value
            j += 1
        i += 1

    return(product_value, value)


# main section
array_list = [4, 4, 72, 10, 721]
found, value = find_product(array_list)
if found:
    print(f"Found a product {value}")
else:
    print("none met the criteria")
print("done")


