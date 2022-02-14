# -*- coding: utf-8 -*-


import brian2 as b2
from neurodynex3.adex_model import AdEx
from neurodynex3.tools import plot_tools, input_factory


# tonic
# a = 0.0*b2.nS; tau_m = 20 * b2.ms; tau_w = 30 * b2.ms; b = 60 * b2.pA; v_reset = -55 * b2.mV

# Adapting
tau_m = 20 * b2.ms; a = 0.0*b2.nS; tau_w = 50 * b2.ms; b = 5 * b2.pA; v_reset = -55 * b2.mV
# Init. burst
# tau_m = 5 * b2.ms; a = 0.5*b2.nS; tau_w = 100 * b2.ms; b = 7 * b2.pA; v_reset = -51 * b2.mV
# bursting
# tau_m = 5 * b2.ms; a = -0.5*b2.nS; tau_w = 100 * b2.ms; b = 7 * b2.pA; v_reset = -46 * b2.mV
# Irregular
# tau_m = 9.9 * b2.ms; a = -0.5*b2.nS; tau_w = 100 * b2.ms; b = 7 * b2.pA; v_reset = -60 * b2.mV
# Transient
# tau_m = 10 * b2.ms; a = 1*b2.nS; tau_w = 100 * b2.ms; b = 10 * b2.pA; v_reset = -60 * b2.mV
# Delayed
# tau_m = 5 * b2.ms; a = -1*b2.nS; tau_w = 100 * b2.ms; b = 10 * b2.pA; v_reset = -60 * b2.mV

current = input_factory.get_step_current(10, 250, 1. * b2.ms, 65.0 * b2.pA)
state_monitor, spike_monitor = AdEx.simulate_AdEx_neuron(I_stim=current, 
                                                         simulation_time=400 * b2.ms,
                                                         tau_m = tau_m, tau_w = tau_w,
                                                         v_reset = v_reset,a = a, b = b,)
plot_tools.plot_voltage_and_current_traces(state_monitor, current)
print("nr of spikes: {}".format(spike_monitor.count[0]))
# AdEx.plot_adex_state(state_monitor)






