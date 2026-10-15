# exotemp.py -- equilibrium temperature of a planet (Pod 3)
# Run from the terminal:  python exotemp.py

import numpy as np

sigma = 5.670e-8      # Stefan-Boltzmann constant, W m^-2 K^-4

# Example inputs: the Sun and Earth, a case where we know the answer.
L = 3.828e26          # star's luminosity, W
d = 1.496e11          # planet's distance from the star, m


def equilibrium_temperature(L, d):
    """Return the equilibrium temperature of a planet, in K.

    Uses T_eq = ( L / (16 pi sigma d^2) )^(1/4), which assumes
    the planet absorbs all the starlight that hits it (no albedo).

    L : star's luminosity, W
    d : planet's distance from the star, m
    """
    # TODO(human):
    #   1. Compute the denominator: 16 * pi * sigma * d squared.
    #      (numpy gives you pi as np.pi)
    #   2. Divide L by that denominator.
    #   3. Raise the result to the 1/4 power, and return it.
    pass
