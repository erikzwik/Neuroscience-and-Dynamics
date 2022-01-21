# -*- coding: utf-8 -*-
import brian2 as b2
import matplotlib.pyplot as plt
from neurodynex3.cable_equation import passive_cable
from neurodynex3.tools import input_factory
import numpy as np
# passive_cable.getting_started()



current = input_factory.get_step_current(1000, 1100, unit_time=b2.us, amplitude=0.8 * b2.namp)
nr_compartments = 100

voltage_monitor, cable_model = passive_cable.simulate_passive_cable(length=0.8 * b2.mm,current_injection_location=[0.2 * b2.mm],
                                                                    nr_compartments = 100, input_current=current, simulation_time = 3*b2.ms)


""" Question 1.1 - Maximum depolarization

probe_location = np.array(0.123 * b2.mm, 0.234 * b2.mm)
v = voltage_monitor[cable_model.morphology[probe_location]].v

# plt.figure()
# plt.imshow(voltage_monitor.v / b2.volt)
# plt.colorbar(label="voltage")
# plt.xlabel("time index")
# plt.ylabel("location index")
# plt.title("vm at (t,x), raw data voltage_monitor.v")
# plt.show()
"""


t = voltage_monitor[cable_model.morphology[0.123*b2.mm]].t
# print(voltage_monitor[cable_model.morphology[0.123*b2.mm]].t)
# # print(np.where([t == 1. * b2.ms, t == 1.1 * b2.ms, t == 1.2 * b2.ms, t == 1.3 * b2.ms]))

# print(cable_model)


""" Question 1.2 - Temporal evolution of different spatial points


all_probe_locations = np.array([0,1,2,3,4,5,6]) * 0.1 * b2.mm
plt.figure()

for probe_location in all_probe_locations:
    v = voltage_monitor[cable_model.morphology[probe_location]].v
    t = voltage_monitor[cable_model.morphology[probe_location]].t
    plt.plot(t,v)


plt.xlabel("time index")
plt.ylabel("voltage")
plt.legend(["0", "100um", "200um", "300um", "400um", "500um", "600um"])
plt.show()
    

"""




""" Question 1.3 - Spatial evolution at different time points


all_time_locations = [100,110,120,130,140,150,160]
all_probe_locations = np.linspace(0,0.79,100) * b2.mm
plt.figure()


for time_location in all_time_locations:
    v_specific = []
    for probe_location in all_probe_locations:
        v_total = voltage_monitor[cable_model.morphology[probe_location]].v
        v_specific.append(v_total[time_location])
        
    plt.plot(all_probe_locations,v_specific)


plt.xlabel("Space")
plt.ylabel("voltage")
plt.legend(["1.0ms", "1.1ms", "1.2ms", "1.3ms", "1.4ms", "1.5ms", "1.6ms"])
plt.show()




"""




# plt.figure()
# plt.imshow(voltage_monitor.v / b2.volt)
# plt.colorbar(label="voltage")
# plt.xlabel("time index")
# plt.ylabel("location index")
# plt.title("vm at (t,x), raw data voltage_monitor.v")
# plt.show()




