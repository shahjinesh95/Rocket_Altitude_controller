"""
rocket_physics.py
Defines the rocket dynamics: forces and state updates.
"""

import numpy as np

def rocket_dynamics(state, thrust, mass, dt, params):
    """
    Update rocket state (altitude, velocity) given thrust and dynamics.

    state: [altitude, velocity]
    thrust: applied thrust [N]
    mass: rocket mass [kg]
    dt: timestep [s]
    params: dict with {"Cd": drag coeff, "A": area, "rho": air density, "g": gravity}

    Returns: new_state [altitude, velocity]
    """
    altitude, velocity = state
    g = params.get("g", 9.81)
    rho = params.get("rho", 1.225)
    Cd = params.get("Cd", 0.5)
    A = params.get("A", 0.01)

    drag = 0.5 * rho * Cd * A * velocity**2 * np.sign(velocity)

    # Net acceleration
    accel = (thrust - drag - mass * g) / mass

    # Update states
    velocity_new = velocity + accel * dt
    altitude_new = altitude + velocity * dt

    return np.array([altitude_new, velocity_new])
