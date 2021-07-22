# We will be building a search engine.
# The input to the search engine's indexing process
# will be a multi line string.  Imagine this is the
# content of a book or a web site.

# The next step of a search engine is to supply a keyword 
# and get the sentences that match. A sentence is defined
# as a string of characters, separated by a period (.)

# The 'index' function takes a 'str' / string
# parameter, finds all unique words and maps them to
# complete sentences.
# The returned value shall be a 'dict' with the 
# keys being each unique word in the original string
# and the values will be a list of full sentences that contain
# that string.
# 
# The 'search' function takes two parameters.
# the first parameter is the 'index/dict' returned from the first function
# the second parameter is a 'keyword' that you should search for
# The returned value should be a unique list of the original 
# sentences that contain the 'keyword'
#
# For this assignment, I'm giving you a __main__ method
# Your job is to make it work. Your functions should match my code
# and my code should execute without error.

# added a new importt
import pandas as pd

def search(index, search_string):

    return_result = []
    return_list = []
    for key in idx.keys():
        if key == search_string:
            return_string = idx[key]
            return_result = return_string.split('.')
            return_result.pop()
            for sentence in return_result:
                return_list.append(sentence + ".")
    return(return_list)


def index(input_string):

    return_dict = {}

    work_string = input_string.strip('\n').lstrip()
    sentence_list = work_string.split('.')
    for sentence in sentence_list:
        word_split = sentence.split(' ')
        for word in word_split:
            s = word.strip(',').strip('\n').strip().lower()
            if s != " " and s != "":
                if s not in return_dict.keys():
                    return_dict[s] = sentence + "."
                else:
                    if sentence not in return_dict[s]:
                        add_string = return_dict[s] + sentence + "."
                        return_dict[s] = add_string
    return(return_dict)

if __name__ == "__main__":
    full_string = """
    Python is an interpreted, interactive, object-oriented programming language. It incorporates modules, exceptions, dynamic typing, very high level dynamic data types, and classes. It supports multiple programming paradigms beyond object-oriented programming, such as procedural and functional programming. Python combines remarkable power with very clear syntax. It has interfaces to many system calls and libraries, as well as to various window systems, and is extensible in C or C++. It is also usable as an extension language for applications that need a programmable interface. Finally, Python is portable: it runs on many Unix variants including Linux and macOS, and on Windows.
    """
    idx = index(full_string)
    if len(idx) != 71:
        raise Exception("Length of idx should have 71 keywords.")
    res = search(idx, "unix")
    if len(res) != 1:
       raise Exception("Length of search results should have 1 line.")
    
    res = search(idx, "finally")
    if len(res) != 1:
        raise Exception("Length of search results should have 1 line.")
        
    res = search(idx, "it")
    if len(res) != 5: 
        raise Exception("Length of search results should have 5 line.")
           
    test_line = "Python is an interpreted, interactive, object-oriented programming language."    
    res = search(idx, "python")
    if len(res) != 3:  
        raise Exception("Length of search results should have 3 line.")
    if test_line not in res:
        raise Exception("The original sentence is not in the results: {}".format(test_line))
    
    res = search(idx, "as")
    if len(res) != 3:  
        raise Exception("Length of search results should have 3 line.")