from math import sqrt, pi

print("comet.py was loaded")   # Task 3: top-level, above the function

# constants
L = 3.8e26       # J/s, solar luminosity
GM = 1.3271e20   # m^3/s^2
h_ice = 2.5e6    # J/kg, energy to sublimate ice
AU = 1.49e11     # m per AU


def dr_per_orbit(R, albedo, rho, a_au, e):
    """Return the radius lost per orbit, in meters."""
    a = a_au * AU
    H_sol = (pi / 2) * (1 - albedo) * R**2 * (L / sqrt(GM)) / sqrt(a * (1 - e**2))
    dM = H_sol / h_ice
    return dM / (4 * pi * R**2 * rho)


if __name__ == "__main__":
    print("running as a script")
    dr = dr_per_orbit(2000.0, 0.0, 500.0, 3.12, 0.5)
    print("dr =", dr, "m per orbit")