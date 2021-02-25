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
I = np.full(len(time),I0)

#Neuron electrical properties
R = 1          #Ohm
C = 0.1       #Farad                
tau = R*C      #10 ms for a typical neuron

# Impulse values in Volt [V]
urest = -0.065
ur = urest
thres = 1 # thres = R*I0 for this type of plotting

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

fig1, ax1 = plt.subplots(1)
#fig2, ax2 = plt.subplots(1)
ax1.set_title('Integrate and Fire Model', )
ax1.plot(time, deltaU/thres, color="orange")
#ax2.plot(time, I)

#Thresholdt
thres_plot = np.full(len(time),thres)
ax1.plot(time,thres_plot,'--')
#Labels
ax1.set_ylabel("Δu(t)/thres", fontsize=15)
#ax2.set_ylabel("Courant [A]")
ax1.set_xlabel("Temps [s]")
#ax2.set_xlabel("Temps [s]")

title = "figures/Tension: C=" + str(C) + ", R=" + str(R) + ",I=" + str(I0) + ".png"

plt.savefig(title)

plt.show()












