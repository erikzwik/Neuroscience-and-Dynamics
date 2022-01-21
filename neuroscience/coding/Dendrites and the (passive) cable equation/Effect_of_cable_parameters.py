# -*- coding: utf-8 -*-


# Exercise 4.3: Effect of cable parameters

import brian2 as b2
import matplotlib.pyplot as plt
from neurodynex3.cable_equation import passive_cable
from neurodynex3.tools import input_factory



b2.defaultclock.dt = 0.005 * b2.ms
simulation_time = 0.2 * b2.ms



# set 1: (same as defaults)
membrane_resistance_1 = 1.25 * b2.Mohm * b2.mm ** 2
membrane_capacitance_1 = 0.8 * b2.uF / b2.cm ** 2
# set 2: (you can think of a myelinated "cable")
membrane_resistance_2 = 5.0 * b2.Mohm * b2.mm ** 2
membrane_capacitance_2 = 0.2 * b2.uF / b2.cm ** 2


current = input_factory.get_step_current(50, 80, unit_time=b2.us, amplitude=0.8 * b2.namp)
voltage_monitor_1, cable_model_1 = passive_cable.simulate_passive_cable(current_injection_location= [400 * b2.um], input_current=current,r_transversal = membrane_resistance_1, simulation_time = simulation_time,capacitance = membrane_capacitance_1)
voltage_monitor_2, cable_model_2 = passive_cable.simulate_passive_cable(current_injection_location= [400 * b2.um], input_current=current,r_transversal = membrane_resistance_2, simulation_time = simulation_time,capacitance = membrane_capacitance_2)






probe_location = 0.49 * b2.mm

# set 1: same as defaults
v_1 = voltage_monitor_1[cable_model_1.morphology[probe_location]].v
t_1 = voltage_monitor_1[cable_model_1.morphology[probe_location]].t

# set 2: "Myelinated cable" 
v_2 = voltage_monitor_2[cable_model_2.morphology[probe_location]].v
t_2 = voltage_monitor_2[cable_model_2.morphology[probe_location]].t



plt.figure()
plt.subplot(211)
plt.plot(t_1 / b2.ms ,v_1 / b2.mV)
plt.title("Temporal voltage evolution at Soma")



plt.subplot(212)
plt.plot(t_2 / b2.ms, v_2 / b2.mV)


plt.xlabel("time index")
plt.ylabel("Voltage")

plt.show()
