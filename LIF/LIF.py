"""
Created on Wed Feb 24 19:24:47 2021

@author: fotis
Integrate-and-fire model. 
Time course of the membrane potential of an integrate-and-fire neuron driven 
by constant input current I0. 
The voltage Δu(t)=u−urest is normalized by the value of the threshold 
Units of input current are chosen so that I0=1 corresponds to a trajectory that 
reaches the threshold for t at inf
After a spike, the potential is reset to ur=urest.


fig1.9 of neuronal dynamims:
https://neuronaldynamics.epfl.ch/online/Ch1.S3.html

"""

import numpy as np
import matplotlib.pyplot as plt


############## TIME #####################
T       =   0.1             # total simulation length [s]
dt      =   0.00001                     # step size [s]
time    =   np.arange(0, T+dt, dt)      # step values [s]


#############Constants###############
#Injected current
I0 = 1.5        #Ampère[A]
I = np.linspace(0,len(time),len(time))
I= np.sin(0.004*I)+1
formuleI = "I=sin(0.004*I0)+1"

#Neuron electrical properties
R = 1          #Ohm
C = 0.02      #Farad                
tau = R*C      #10 ms for a typical neuron

# Impulse values in Volt [V]
urest = -0.065
ur = urest
thres = R # thres = R*I0=R*1 for this type of plotting(I0 normalization=0)

def LIF_num(I,R,C):
    # Voltage initialization
    u = np.empty(len(time))
    u[0] = urest
    
    #Prediction at t 
    for t in range(1,len(time)):
        #Differential equation
        uprime =  (1/tau) * (R*I[t] - (u[t-1]-urest))
        u[t] = u[t-1] + uprime*dt
        
        #Spike at threshold
        if u[t]-urest >= thres:
            u[t] = ur
    return u

######DATA GENERATION##########
#Generate voltage
u = LIF_num(I,R,C)
deltaU = u - urest


#######Plotting#############
###Tension plot#####
fig1, ax1 = plt.subplots(1)
ax1.set_title('Integrate and Fire Model', )
ax1.plot(time, deltaU/thres, color="orange")
ax1.set_ylabel("Δu(t)/thres", fontsize=15)
ax1.set_xlabel("Temps [s]")
thres_plot = np.full(len(time),thres)
ax1.plot(time,thres_plot,'--')

title = "figures/Tension: C=" + str(C) + ", R=" + str(R) + "," + formuleI + " avec I0=" + str(I0) + ".png"

plt.savefig(title)
'''
###Courant plot###
fig2, ax2 = plt.subplots(1)
ax2.plot(time, I)
ax2.set_ylabel("Courant [A]")
ax2.set_xlabel("Temps [s]")
'''
plt.show()












