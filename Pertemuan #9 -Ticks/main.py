#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 16:31:03 2019

@author: rafliano
"""

import matplotlib.pyplot as plt
import numpy as np

# membuat data
sudut = np.arange(0,360,1)
y = np.sin(np.deg2rad(sudut))

# buat plot

plt.plot(sudut,y)
plt.ylabel('magnituda')
plt.xlabel('sudut')


plt.yticks([-1,0,1])
plt.xticks(
    [0,     90,    180     ,270       ,360],
    [r'${0}^o$',r'${90}^o$',r'${180}^o$',r'${270}^o$',r'${360}^o$',])

# tampilkan plot

plt.show()