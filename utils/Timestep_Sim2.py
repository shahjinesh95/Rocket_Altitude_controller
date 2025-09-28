"""
simulation_engine.py
Time-stepping simulation for the rocket.
"""

import numpy as np
from rocket_physics import rocket_dynamics

def simulate(initial_state, thrust_fn, mass, dt, t_final, params):
    """
    Run simulation loop.

    thrust_fn: function(time, state) -> thrust
    """
    steps = int(t_final / dt)
    states = np.zeros((steps, 2))
    times = np.linspace(0, t_final, steps)

    state = np.array(initial_state)
    for i, t in enumerate(times):
        thrust = thrust_fn(t, state)
        state = rocket_dynamics(state, thrust, mass, dt, params)
        states[i] = state

    return times, states
