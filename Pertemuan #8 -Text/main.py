#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 13:33:23 2019

@author: rafliano
"""

import matplotlib.pyplot as plt
import numpy as np


# Membuat Data
def sinusGenerator(amplitudo,frekuensi,tAkhir,theta):
	t = np.arange(0,tAkhir,0.1)
	y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
	return t,y

t,y = sinusGenerator(1,1,4,0)

plt.plot(t,y)
plt.text(2,0.5, r'$ y = \mathcal{A}.sin(2 \omega t)$')
plt.text(2,0.4, r'$ \mathcal{a} = 1 cm, \omega = 1Hz$')

plt.show()