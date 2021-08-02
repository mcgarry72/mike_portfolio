def swap_case(s):
    return_string = str()
    for char in s:
        if char.isupper():
            return_string += char.lower()
        elif char.islower():
            return_string += char.upper()
        else:
            return_string += char

    return return_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)