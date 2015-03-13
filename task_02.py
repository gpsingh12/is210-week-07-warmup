#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module import another module named data
   and perform operations on the list using
   operators del, slice, append and extend.
"""

import data
BALLETS = data.BALLETS

del BALLETS[11]
BALLETS[1] = 'Swan Lake'
BALLETS.append('Herman Schmerman')
BALLETS.extend(['Don Quixote', 'Sylvia'])
