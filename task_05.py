#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module uses for loop and proporties
   of lists to reverse elements of list.
"""


def flip_keys(to_flip):
    """Function takes one argument and returns
       the reversed input nested, immutable list.
       Args:
           counter(int): the variable to increment the index
                         while using for loop.
            to_flip(mixed): the input immutable, nested list.
        Returns:
                returns the inner sequence items of list in
                reverse order.
        Examples:
                >>> flip_keys([(1, 2, 3), 'hello'])
                    [(3, 2, 1), 'hello']
                    [(3, 2, 1), 'olleh']
    """
    counter = 0
    for item in to_flip:

        to_flip[counter] = item[::-1]

        counter += 1

    return to_flip
