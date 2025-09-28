"""
utils_plotting.py
Reusable plotting utilities.
"""

import matplotlib.pyplot as plt

def plot_states(times, states, setpoint=None):
    altitude = states[:, 0]
    velocity = states[:, 1]

    plt.figure(figsize=(10,5))

    plt.subplot(2,1,1)
    plt.plot(times, altitude, label="Altitude")
    if setpoint is not None:
        plt.axhline(setpoint, color="r", linestyle="--", label="Setpoint")
    plt.ylabel("Altitude [m]")
    plt.legend()

    plt.subplot(2,1,2)
    plt.plot(times, velocity, label="Velocity")
    plt.ylabel("Velocity [m/s]")
    plt.xlabel("Time [s]")
    plt.legend()

    plt.tight_layout()
    plt.show()
