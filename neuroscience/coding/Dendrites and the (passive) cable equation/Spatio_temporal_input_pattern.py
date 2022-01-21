# -*- coding: utf-8 -*-

# Exercise 4.2: Spatio-temportal input pattern

import brian2 as b2
import matplotlib.pyplot as plt
from neurodynex3.cable_equation import passive_cable
from neurodynex3.tools import input_factory

""" Getting started
t_spikes = [10, 15, 20]
l_spikes = [100. * b2.um, 200. * b2.um, 300. * b2.um]
current = input_factory.get_spikes_current(t_spikes, 100*b2.us, 0.8*b2.namp, append_zero=True)
voltage_monitor_ABC, cable_model = passive_cable.simulate_passive_cable(current_injection_location=l_spikes, input_current=current)
"""

""" Introduction plot

plt.figure()
plt.imshow(voltage_monitor_ABC.v / b2.volt)
plt.colorbar(label="voltage")
plt.xlabel("time index")
plt.ylabel("location index")
plt.title("vm at (t,x), raw data voltage_monitor.v")
plt.show()

"""



""" Question 2.1 Temporal evolution of membrane voltage at soma

probe_location = 0. * b2.um
v = voltage_monitor_ABC[cable_model.morphology[probe_location]].v
t = voltage_monitor_ABC[cable_model.morphology[probe_location]].t


plt.figure()
plt.plot(t,v)
plt.xlabel("time index")
plt.ylabel("Voltage")
plt.title("Temporal voltage evolution at Soma")
plt.show()

""" 


# """ Question 2.2 Same as Q 2.1, but reversed order of input spikes


t_spikes = [10, 15, 20]
l_spikes = [300. * b2.um, 200. * b2.um, 100. * b2.um]
current = input_factory.get_spikes_current(t_spikes, 100*b2.us, 0.8*b2.namp, append_zero=True)
voltage_monitor_ABC, cable_model = passive_cable.simulate_passive_cable(current_injection_location=l_spikes, input_current=current)




probe_location = 0. * b2.um
v = voltage_monitor_ABC[cable_model.morphology[probe_location]].v
t = voltage_monitor_ABC[cable_model.morphology[probe_location]].t


plt.figure()
plt.plot(t,v)
plt.xlabel("time index")
plt.ylabel("Voltage")
plt.title("Temporal voltage evolution at Soma")
plt.show()






# """