#!/usr/bin/python3
""" Defines a method to check UTF8 Valid integers """


def validUTF8(data):
    """ Checks UTF8 Valid data set """

    for byt in data:
        bin_char = format(byt, '08b')

        if bin_char.startswith('0'):
            continue
        elif bin_char.startswith('110'):
            continue
        elif bin_char.startswith('1110'):
            continue
        elif bin_char.startswith('11110'):
            continue
        else:
            return False
    return True
