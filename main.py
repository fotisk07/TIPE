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

lpfreq = 20
rms = np.sqrt(np.mean(y1**2))

hp = signal.butter(10, 20, 'hp', fs=1000, output='sos')
#filtered = signal.sosfilt(hp, y1)
rectified = np.abs(y1-rms)


lp = signal.butter(50, lpfreq, 'lp', fs=1000, output='sos')
output = signal.sosfilt(lp,rectified)





fig, (ax1, ax2) = plt.subplots(2, sharex=True)
fig.suptitle('Raw and Rectified Signals')
ax1.plot(time, y1)
ax2.plot(time, rectified,'y')
ax1.set_title("Raw signal")
ax2.set_title("Rectified signal")
ax2.set_xlabel("Time (ms) ")
plt.savefig("Resultats/Filtered_and_rectified.png")



fig3, ax3 = plt.subplots()
ax3.plot(time, output,'m')
ax3.set_title("Output signal")
ax3.set_xlabel("time")
name = "Resultats/Output with coupure at " + str(lpfreq) + ".png"

plt.savefig(name)
