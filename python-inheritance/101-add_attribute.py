#!/usr/bin/python3
'''Module for add_attribute method'''


def add_attribute(obj, name, value):
    '''Function that adds a new attribute to an object if it is possible'''
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
