# -*- coding: utf-8 -*-

from neurodynex3.leaky_integrate_and_fire import LIF
from neurodynex3.tools import input_factory, plot_tools
import brian2 as b2
print("resting potential: {}".format(LIF.V_REST))


# create a step current with amplitude = I_min
step_current = input_factory.get_step_current(
    t_start=5, t_end=500, unit_time=b2.ms, 
    amplitude=3e-3*b2.uamp)  # set I_min to your value

V_REST = -60*b2.mV
# run the LIF model.
# Note: As we do not specify any model parameters, the simulation runs with the default values
(state_monitor,spike_monitor) = LIF.simulate_LIF_neuron(
    input_current=step_current, simulation_time = 500 * b2.ms, v_rest = -60*b2.mV)

# plot I and vm
plot_tools.plot_voltage_and_current_traces(
state_monitor, step_current, title="min input", firing_threshold=LIF.FIRING_THRESHOLD)
print("nr of spikes: {}".format(spike_monitor.count[0]))  # should be 0

