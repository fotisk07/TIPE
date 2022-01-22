#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 19:49:43 2021

@author: fotis
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sg



def get_single_column_data(filepath):

    with open(filepath,"r") as file:
        data = file.read()



    data = [int(s) for s in data.split() if s.isdigit()]
    return np.array(data)


def get_double_column_data(filepath):
    with open(filepath,"r") as file:
        data = file.read()

    data = data.split('=')
    
    raw = data[1:len(data):2]
    filtered = data[2:len(data):2]
    
    raw_list = '\n'.join(raw)
    
    filtered_list = '\n'.join(filtered)
    #print(filtered_list)
    raw_signal = [int(s) for s in raw_list.split() if s.isdigit()]
    filtered_signal = [int(s) for s in filtered_list.split() if s.isdigit()]
    
    return np.array(raw_signal), np.array(filtered_signal)
 
   
   

def create_time_axes(data):
    return np.linspace(0,np.size(data)*4,np.size(data))


def filter(signal, lpfreq,order, highpass = False, plot=False):
    rms = np.sqrt(np.mean(signal**2))
    if highpass == True:
        hp = sg.butter(1, 5, 'hp', fs=1000, output='sos')
        signal = sg.sosfilt(hp, signal)
        
    rectified_signal = np.abs(signal-rms)
    lp = sg.butter(order, lpfreq, 'lp', fs=1000, output='sos',)
    output = sg.sosfilt(lp,rectified_signal)
    
    if plot==True:
        time = create_time_axes(signal)
        fig, ax = plt.subplots()
        ax.plot(time, output,'m')
        ax.set_title("Output signal")
        ax.set_xlabel("time")
    
    return output












