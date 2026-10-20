# exotemp.py -- equilibrium temperature of a planet (Pod 3)
# Run from the terminal:  python exotemp.py

import math


sigma = 5.670e-8      # Stefan-Boltzmann constant, W m^-2 K^-4

# Example inputs: the Sun and Earth, a case where we know the answer.
L = 3.828e26          # star's luminosity, W
d = 1.496e11          # planet's distance from the star, m
 denom = 16 * math.pi * sigma * d ** 2


if __name__ == '__main__':
    # sys.argv holds the command-line words as strings:
    #   sys.argv[0] is the script name, [1] is L, [2] is d
    L = float(input('Luminosity'))
    d = float(input('Distance'))
    T = equilibrium_temperature(L, d)
    print(f"{T:.1f} K")
