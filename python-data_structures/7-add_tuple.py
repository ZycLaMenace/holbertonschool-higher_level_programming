#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    a = a[:2]
    b = b[:2]
    sum_1 = a[0] + b[0]
    sum_2 = a[1] + b[1]
    return (sum_1, sum_2)
