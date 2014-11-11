#!/usr/bin/python
# Filename : one_more_variable.py
def powersum(power, *args):
    """
    :param power:
    :param args:
    :return:
    """
    total = 0
    for i in args:
        total += pow(i, power)
    return total

print powersum(2, 3, 4)

def foo(**kwargs):
    """

    :param kwargs:
    :return:
    """
    for i in kwargs:
        print i, "-->", kwargs[i]

foo(one="first",two="second")