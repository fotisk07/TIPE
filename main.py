#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 20:55:41 2021

@author: fotis
"""
import matplotlib.pyplot as plt
from helper import *

#
#y1,y2 = get_double_column_data("Signaux/rnf1.txt")
#
#time = create_time_axes(y1)
#
#plt.plot(time,y1,'-')
#plt.plot(time,y2,'-')
#plt.show()
#plt.savefig("Resultats/Processed and raw signal")
#

y1 = get_single_column_data("Signaux/raw2.txt")
time = create_time_axes(y1)

plt.plot(time,y1)
plt.show()
plt.savefig("Raw signal 2")
