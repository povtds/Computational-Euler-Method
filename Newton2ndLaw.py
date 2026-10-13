# TDS Numerical Python Operations for NUMMET Practical (22nd May 2025)
# Importing the Required Numerical Python Packages :
# Avoid Indentation-Errors
###############################################################################
import numpy as TDS
import matplotlib.pyplot as plt
###############################################################################

# Initial Conditions and Parameters :
F = 1.0       # Constant Force (N)
v0 = 1.0      # Initial Velocity (m/s)
x0 = 0.0      # Initial Position (m)
m = 1.0       # Mass (kg)
t_max = 10.0  # Total Time (s)
dt = 0.01     # Time step

# Parameters:
#    - v0: Initial velocity
#    - x0: Initial position
#    - m: Mass
#    - t_max: Maximum time to simulate
#    - dt: Time step size

# Returns:
#    - t: array of time
#    - x: array of position at each time
#    - v: array of velocity at each time

# Number of Steps :
N = int(t_max / dt)

# Initializing Arrays for Time, Position, and Velocity :
time_points = TDS.linspace(0, t_max, N + 1)
positions = TDS.zeros(N + 1)
velocities = TDS.zeros(N + 1)

# Set initial conditions
initial_position = positions[0] 
initial_velocity = velocities[0]


# Euler's Method Loop
for n in range(N): # Using The For-Loop for a Fixed Number of Time-Steps
    # Calculate acceleration (using Newton's 2nd Law: a = F/m)
    acceleration = F / m

    # Update velocity using Euler's method: v(t+dt) = v(t) + a(t) * dt
    velocities [n + 1] = velocities[n] + acceleration * dt

    # Update position using Euler's method: x(t+dt) = x(t) + v(t) * dt
    # Note: We use the velocity at the *current* time step for the position update
    positions [n + 1] = positions[n] + velocities[n] * dt

# Creating the Line Graphs and Adding Labels :

# 1) Plotting Position vs Time :
plt.figure() # Create a New Figure to Avoid Overlapping Another Plot
plt.plot(time_points, positions, label="Position vs Time (Euler's Method)", color='purple')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title("Newton's 2nd Law - Position (m) vs Time (s)")
plt.legend()
plt.grid(True)
plt.show()

# 2) Plotting Velocity vs Time :
plt.figure() # Create Another New Figure
plt.plot(time_points, velocities, label="Velocity vs Time (Euler's Method)", color='orange')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title("Newton's 2nd Law - Velocity (m/s) vs Time (s)")
plt.legend()
plt.grid(True)
plt.show()

