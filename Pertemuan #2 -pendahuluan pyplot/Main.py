#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 20:37:43 2019

@author: rafliano
"""

import numpy as np
import matplotlib.pyplot as plt

"""
    1. Membuat data
    2. Membuat plot
    3. Menampilkan Plot
"""

# 1. Membuat data
x = np.array([1,2,3,4,5])
y = np.array([1,4,9,16,25])
y2 = np.array([1,16,81,256,625])

# 2. Membuat plot
plt.plot(x,y)
plt.plot(x,y2)

# 3. Menampilkan plot
plt.show()