#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module uses a for loop to perform the
   arithmetic functions.
"""


def process_data(data):
    """Function takes one argument named data and
       uses a for loop to get sum and average of
       input data.
       Arg:
           total(int): sum of the input data.
           average(float): average of input data.
       Return:
           returns a tuple providing sum and average of
           input data.
       Examples:
                >>> process_data([1, 2, 3])
                    (6, 2.0)
    """
    value = 0
    for total in data:
        value += total

    average = (value/float(len(data)))
    return value, average
