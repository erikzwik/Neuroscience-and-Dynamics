# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 16:04:14 2022

@author: erik
"""

# Exercise 4.4: Stationary soluton and comparison with theoretical result

import brian2 as b2
import matplotlib.pyplot as plt
import numpy as np
from neurodynex3.cable_equation import passive_cable
from neurodynex3.tools import input_factory



sim_time = 100 * b2.ms
N_comp = 100; 


b2.defaultclock.dt = 0.1 * b2.ms
current = input_factory.get_step_current(0, 0, unit_time=b2.ms, amplitude=0.1 * b2.namp, append_zero=False)
voltage_monitor, cable_model = passive_cable.simulate_passive_cable(
length=0.5 * b2.mm, current_injection_location = [0*b2.um],
input_current=current, simulation_time=sim_time, nr_compartments=N_comp)
v_X0 = voltage_monitor.v[0,:]  # access the first compartment
v_Xend = voltage_monitor.v[-1,:]  # access the last compartment
v_Tend = voltage_monitor.v[:, -1]  # access the last time step


v_t100 = np.linspace(0,100,1000) * b2.ms


plt.figure()
plt.plot(v_t100, v_X0)
plt.xlabel("time index")
plt.ylabel("location index")
plt.title("vm at 500 um")
plt.show()








