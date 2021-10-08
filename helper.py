#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 19:49:43 2021

@author: fotis
"""

import numpy as np



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
    
    raw_signal = [int(s) for s in raw_list.split() if s.isdigit()]
    filtered_signal = [int(s) for s in filtered_list.split() if s.isdigit()]
    
    return raw_signal, filtered_signal
 
   
   

def create_time_axes(data):
    return np.linspace(0,np.size(data)*2,np.size(data))

