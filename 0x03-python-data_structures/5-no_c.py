#!/usr/bin/python3
def no_c(my_string: str):
    my_string = ''.join(my_string.split('c'))
    my_string = ''.join(my_string.split('C'))
    return my_string
