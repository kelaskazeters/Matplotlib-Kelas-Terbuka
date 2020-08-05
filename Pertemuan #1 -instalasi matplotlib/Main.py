#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 20:28:55 2019

@author: rafliano
"""

import numpy as np
import matplotlib.pyplot as plt

# kita buat lingkaran
PI = np.pi
sudut = np.linspace(0,2*PI,100)
radius = 5;

x = radius * np.cos(sudut)
y = radius * np.sin(sudut)

# insialisasi plot
plt.plot(x,y)

# tampilkan
plt.show()