#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module uses for loop and proporties
   of lists to reverse elements of list.
"""
def flip_keys(to_flip):
    """
    """
    counter = 0
    for item in to_flip:
        counter += 1
        to_flip[counter] = to_flip[::-counter] #using counter as index to
        # replace the values of items
    print to_flip

    
    
