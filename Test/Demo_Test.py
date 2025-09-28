"""
demo_run.py
Integrates physics, simulation, controller, and plotting for demo.
"""

import numpy as np
from simulation_engine import simulate
from controller_design import PIDController
from utils_plotting import plot_states

# Parameters
params = {"g": 9.81, "rho": 1.225, "Cd": 0.5, "A": 0.01}
mass = 50  # kg
dt = 0.01
t_final = 10
setpoint = 100  # target altitude

# Controller
pid = PIDController(kp=20, ki=5, kd=10, u_min=0, u_max=200)

def thrust_fn(t, state):
    altitude, velocity = state
    return pid.update(setpoint, altitude, dt)

# Run simulation
times, states = simulate([0, 0], thrust_fn, mass, dt, t_final, params)

# Plot results
plot_states(times, states, setpoint=setpoint)
