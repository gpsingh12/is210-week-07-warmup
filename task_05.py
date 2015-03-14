#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module uses for loop and proporties
   of lists to reverse elements of list.
"""
def flip_keys(to_flip):
    """
    """
    #to_flip[::-1]
    counter = []
    for item in to_flip:
       counter.extend(item[::-1])
    print counter

