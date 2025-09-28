# Rocket_Altitude_controller-

Rocket physics-
    Contains the equations of motion mass, thrust, drag, gravity
    Defines functions for updateing rocket dynamics given inputs
    Test, simulate free fall and constant thrust cases
Simulation
    A time step simulation loop numerical integrator, eg, Euler RK4
    Calls physics function to advance state
    Test, Run simulation with constant thrust and plot trajectory
Controller design
    Controler implementations PID, Clamped control, bang bang
    Functions take rocket state + desired altitude - output thrust command
    Test: step response control for reaching setpoint altitude
util plotting 
    Plotting utilities, altitude vs time, velocity , control effor
    Reusable code for all steps
    Test, plot sample sine/cosine signals
Demo test
    Integrates all module: physics, simulation controller, plotting
    Runs pull demo scenario (eg target altitude tracking)
    Test, ensure output plots+final altitude error are correct


