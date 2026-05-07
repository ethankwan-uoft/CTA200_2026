'''
@mandelbrot_map.py
@author: Ethan Kwan
@May 5, 2026
@iteration function used for assignment 3, question 1.

'''

import numpy as np

def diverge_when(c, z0=0, max_iter=30):
    """
    This function finds whether a given point c on the complex plane converges or diverges after iterating through the equation z_{i+1} = z_{i}^2 + c.
    
    Parameters:
    c, complex, the point on the complex plane
    z0, float, the starting value
    max_iter, int, the maximum number of times the function is applied before a verdict is reached
    
    Returns:
    n: the number of iterations it takes for the point to diverge. Divergence defined as ||z|| > 100. If the point does not diverge, then returns None.
    """
    
    n = 0
    z = z0
    while (n < max_iter) and (np.abs(z) <= 100):
        z = z**2 + c
        n = n + 1
    
    if np.abs(z) <= 100:
        #it's bounded
        return
    
    #otherwise, it diverged before n hit max_iter
    return n
    