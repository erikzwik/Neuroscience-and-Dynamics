# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 11:50:39 2022

@author: erik
"""

# 6. FitzHugh-Nagumo: Phase plane and bifurcation analysis


# =============================================================================
# %matplotlib inline
# =============================================================================

import brian2 as b2
import matplotlib.pyplot as plt
import numpy as np
from neurodynex3.phase_plane_analysis import fitzhugh_nagumo

# Intro


# fitzhugh_nagumo.plot_flow()

# fixed_point = fitzhugh_nagumo.get_fixed_point()
# print("fixed_point: {}".format(fixed_point))

# plt.figure()
# trajectory = fitzhugh_nagumo.get_trajectory()
# plt.plot(trajectory[0], trajectory[1])








# Question 1.1

# x = np.arange(-2.5, 2.51, .1)  # create an array of x values
# y = -x**2 / 2. + x + 1  # calculate the function values for the given x values
# plt.plot(x, y, color='black')  # plot y as a function of x
# plt.xlim(-2.5, 2.5)  # constrain the x limits of the plot


# I = 0
# e = 0.1

# u = np.arange(-2.5, 2.51, .1)
# # u - nullcline and w - nullcline respectively
# nullc = np.array([u*(1-u**2), 2*u + 2]).T
# plt.plot(u, nullc)
# plt.show()



# Question 1.2

# u_0 = 0
# w_0 = 0
# I = 1.3
# eps = 0.1
# t, u, w = fitzhugh_nagumo.get_trajectory(u_0, w_0, I)


# plt.plot(u,w)
# plt.show()


# u = np.arange(-1.5, 1.01, .1)
# # u - nullcline and w - nullcline respectively
# nullc = np.array([u*(1-u**2)+I, 2*u + 2]).T

# plt.plot(u, nullc)
# plt.show()




# Question 1.3


u_0 = 0
w_0 = 0
I = 1.2570262
eps = 0.1
t, u, w = fitzhugh_nagumo.get_trajectory(u_0, w_0, I)



plt.plot(u,w)
fitzhugh_nagumo.plot_flow(I,eps)


u = np.arange(-1.5, 1.01, .1)
# u - nullcline and w - nullcline respectively
nullc = np.array([u*(1-u**2)+I, 2*u + 2]).T

plt.plot(u, nullc)
plt.show()