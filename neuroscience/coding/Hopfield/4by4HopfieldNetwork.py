# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 11:28:16 2022

@author: erik
"""

from neurodynex3.hopfield_network import network, pattern_tools, plot_tools
import matplotlib.pyplot as plt
pattern_size = 4

# create an instance of the class HopfieldNetwork
hopfield_net = network.HopfieldNetwork(nr_neurons= pattern_size**2)
plot_tools.plot_network_weights(hopfield_net)
# instantiate a pattern factory
factory = pattern_tools.PatternFactory(pattern_size, pattern_size)
# create a checkerboard pattern and add it to the pattern list


checkerboard = factory.create_checkerboard()
# pattern_list = [checkerboard]


l_pattern = factory.create_L_pattern()
pattern_list = [checkerboard]



hopfield_net.store_patterns(pattern_list)
# plot_tools.plot_network_weights(hopfield_net)


plt.figure()
plt.hist(hopfield_net.weights.flatten())


# # add random patterns to the list
# pattern_list.extend(factory.create_random_pattern_list(nr_patterns=4, on_probability=0.5))
# plot_tools.plot_pattern_list(pattern_list)
# # how similar are the random patterns and the checkerboard? Check the overlaps
# overlap_matrix = pattern_tools.compute_overlap_matrix(pattern_list)
# plot_tools.plot_overlap_matrix(overlap_matrix)

# # let the hopfield network "learn" the patterns. Note: they are not stored
# # explicitly but only network weights are updated !
# hopfield_net.store_patterns(pattern_list)

# # create a noisy version of a pattern and use that to initialize the network
# noisy_init_state = pattern_tools.flip_n(pattern_list[0], nr_of_flips=5)
# hopfield_net.set_state_from_pattern(noisy_init_state)

# # from this initial state, let the network dynamics evolve.
# states = hopfield_net.run_with_monitoring(nr_steps=5)

# # each network state is a vector. reshape it to the same shape used to create the patterns.
# states_as_patterns = factory.reshape_patterns(states)
# # plot the states of the network
# plot_tools.plot_state_sequence_and_overlap(states_as_patterns, pattern_list, reference_idx=0, suptitle="Network dynamics")