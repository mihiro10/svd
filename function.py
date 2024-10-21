import numpy as np
import matplotlib.pyplot as plt

def compute_original_function(x, time):
    """
    Computes the value of the original function f(x, t).

    Parameters:
    x (float or ndarray): Spatial variable.
    time (float): Temporal variable.

    Returns:
    float or ndarray: The computed value of the original function at (x, t).
    """
    return (np.pi**2 - 1) * np.exp(-time) * np.sin(np.pi * x)