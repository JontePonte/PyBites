
'''
Write a function that rotates characters in a string, in both directions:

if n is positive move characters from beginning to end, e.g.: rotate('hello', 2) would return llohe
if n is negative move characters to the start of the string, e.g.: rotate('hello', -2) would return lohel
See tests for more info. Have fun!
'''


def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    # separate first and last part of string
    string_split_first = string[0:n]
    string_split_last = string[n:]

    # combine them reversed, could be made shorter but this is easier to reed
    return string_split_last + string_split_first


print(rotate("hello", 0))