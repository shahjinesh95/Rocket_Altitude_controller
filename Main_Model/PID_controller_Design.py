"""
controller_design.py
Implements controllers (PID, bang-bang).
"""

class PIDController:
    def __init__(self, kp, ki, kd, u_min=0, u_max=100):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.integral = 0
        self.prev_error = 0
        self.u_min = u_min
        self.u_max = u_max

    def update(self, setpoint, measurement, dt):
        error = setpoint - measurement
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt
        self.prev_error = error

        u = self.kp * error + self.ki * self.integral + self.kd * derivative
        return max(self.u_min, min(self.u_max, u))
