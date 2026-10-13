import numpy as np

# Estimates how many orbits a spherical comet survives, given that sunlight sublimates ice from
# its surface each time it passes the Sun.

from math import sqrt, pi

# constants
L = 3.8e26      # J/s, solar luminosity
GM= 1.3271e20  # m^3/s^2
hi= 2.5e6       # J/kg, energy to sublimate ice
AU = 1.49e11        # m per AU

# inputs
R_km = float(input("Comet radius in km: "))
A = float(input("Albedo (0 to 1): "))
a_AU = float(input("Semi-major axis in AU: "))
e = float(input("Eccentricity: "))
rho = float(input("Density in kg/m^3: "))

# convert to SI
R = R_km * 1000     # m
a = a_AU * AU       # m

# calculation
H_sol = (pi / 2) * (1 - A) * R**2 * (L/ sqrt(GM)) / sqrt(a * (1 - e**2))
dM = H_sol / hi                  # kg lost per orbit
dr = dM / (4 * pi * R**2 * rho)     # m of radius lost per orbit
orbits = R / dr
period = a_AU**1.5                 # years per orbit
lifetime = orbits * period          # years

print(f"The comet shrinks by {dr:.2f} m per orbit, so it has about {orbits:.0f} orbits left, "
      f"which is about {lifetime:.0f} years.")