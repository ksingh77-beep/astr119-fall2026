# exotemp.py -- equilibrium temperature of a planet (Pod 3)
# Run from the terminal:  python exotemp.py

import numpy as np

# Example inputs: the Sun and Earth, a case where we know the answer.
T_star = 5772.0       # star's effective temperature, K
R_star = 6.957e8      # star's radius, m
a = 1.496e11          # planet's orbital distance (semi-major axis), m
albedo = 0.30         # fraction of starlight the planet reflects, no units


def equilibrium_temperature(T_star, R_star, a, albedo):
    """Return the equilibrium temperature of a planet, in K.

    T_star : star's effective temperature, K
    R_star : star's radius, m
    a      : planet's orbital distance, m (same units as R_star)
    albedo : fraction of light reflected, between 0 and 1
    """
    # TODO(human):
    #   1. Compute the ratio R_star / (2 * a).
    #   2. Take its square root.
    #   3. Compute (1 - albedo) to the 1/4 power.
    #   4. Multiply T_star by the results of steps 2 and 3, and return it.
    pass
