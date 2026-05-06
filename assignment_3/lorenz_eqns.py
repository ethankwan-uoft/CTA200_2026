'''
@lorenz_eqns.py
@author: Ethan Kwan
@May 6, 2026
@Lorenz equations used for assignment 3, question 2.

'''

def lorenz(t, v, sigma, r, b):
    """
    System of Lorenz equations used for the right-hand side of solve_ivp.
    
    Parameters:
    t, time
    v, vector of [x, y, z]
    sigma, float, the Prandtl number
    r, float, the Rayleigh number
    b, float, dimensionless length scale
    
    Returns:
    vdot, vector of the time derivatives [xdot, ydot, zdot]
    """
    x, y, z = v
    xdot = -1 * sigma * (x - y)
    ydot = r * x - y - x * z
    zdot = -b * z + x * y
    
    return [xdot, ydot, zdot]
    