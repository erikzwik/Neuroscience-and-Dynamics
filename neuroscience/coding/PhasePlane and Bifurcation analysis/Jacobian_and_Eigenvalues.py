# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 08:14:04 2022

@author: erik
"""


# Exercise 2: Jacobian & Eigenvalues


import brian2 as b2
import matplotlib.pyplot as plt
import numpy as np
from neurodynex3.phase_plane_analysis import fitzhugh_nagumo


def get_jacobian(u_0,w_0):
    return [[1-3*u_0**2, -1],[0.1, -0.05]]


I = 0.0

u_0, w_0 = fitzhugh_nagumo.get_fixed_point(I)

J = get_jacobian(u_0, w_0)

    
eigs = np.linalg.eigvals(J)

print(eigs)



# Exercise 3: Bifurcation analysis

list1 = []
list2 = []
currents = np.arange(0,4,.1) # the I values to use
for I in currents:
    # your code to calculate the eigenvalues e = [e1,e2] for a given I goes here
    u_0, w_0 = fitzhugh_nagumo.get_fixed_point(I)
    J = get_jacobian(u_0, w_0)
    e = np.linalg.eigvals(J)
    
    list1.append(e[0].real) # store each value in a separate list
    list2.append(e[1].real)
    
plt.plot(currents, list1)
plt.plot(currents, list2)
plt.show()
