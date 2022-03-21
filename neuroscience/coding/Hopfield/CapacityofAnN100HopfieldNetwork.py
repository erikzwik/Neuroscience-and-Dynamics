# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 07:42:27 2022

@author: erik
"""

#Question 7.4.2
# N = 10*10 = 100. C_store = 0.138. --> M = 100*0.138 = 13.8
 
from neurodynex3.hopfield_network import network, pattern_tools, plot_tools
import matplotlib.pyplot as plt

pattern_size = 10


hopfield_net = network.HopfieldNetwork(nr_neurons= pattern_size**2)

factory = pattern_tools.PatternFactory(pattern_size, pattern_size)
# create a checkerboard pattern and add it to the pattern list
checkerboard = factory.create_checkerboard()
pattern_list = [checkerboard]


# add random patterns to the list
pattern_list.extend(factory.create_random_pattern_list(nr_patterns=13, on_probability=0.5))
plot_tools.plot_pattern_list(pattern_list)
# how similar are the random patterns and the checkerboard? Check the overlaps
overlap_matrix = pattern_tools.compute_overlap_matrix(pattern_list)
plot_tools.plot_overlap_matrix(overlap_matrix)

# let the hopfield network "learn" the patterns. Note: they are not stored
# explicitly but only network weights are updated !
hopfield_net.store_patterns(pattern_list)

# create a noisy version of a pattern and use that to initialize the network
checkboard_init_state = pattern_tools.flip_n(pattern_list[0], nr_of_flips=0)
hopfield_net.set_state_from_pattern(checkboard_init_state)

# from this initial state, let the network dynamics evolve.
states = hopfield_net.run_with_monitoring(nr_steps=5)

# each network state is a vector. reshape it to the same shape used to create the patterns.
states_as_patterns = factory.reshape_patterns(states)
# plot the states of the network
plot_tools.plot_state_sequence_and_overlap(states_as_patterns, pattern_list, reference_idx=0, suptitle="Network dynamics")