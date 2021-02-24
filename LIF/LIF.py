#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 19:24:47 2021

@author: fotis
"""

import numpy as np
import matplotlib.pyplot as plt

# TIME
T       =   0.3                # total simulation length [s]
dt      =   0.00002                     # step size [s]
time    =   np.arange(0, T+dt, dt)      # step values [s]


def LIF(I,R,C):
    urest = -0.065
    thres = -0.035
    spike = 0.040
    tau = R*C
    
    u = np.empty(len(time))
    u[0] = urest
    
    
    for t in range(1,len(time)):
        du =  (1/tau) * (R*I[t] - (u[t-1]-urest))
        u[t] = u[t-1] + du*dt
        
        if u[t] > thres:
            u[t-1] = spike
            u[t] = urest
            
    return u

    
I = np.zeros(len(time))
I[2000:6000] = 0.005

     
y = LIF(I,150,0.005)
plt.plot(time,y)
plt.ylabel("Potentiel [V]")
plt.xlabel("Temps [s]")
plt.title("Modèle LIF")
plt.savefig("LIF.png")
plt.show()