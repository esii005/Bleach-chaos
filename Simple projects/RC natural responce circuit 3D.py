import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Define circuit parameters
R = 10e3  # Resistance in ohms (10kΩ)
C = 10e-6  # Capacitance in farads (10µF)
V0 = 5  # Initial voltage in volts

# Time setup
tau = R * C  # Time constant (RC)
t = np.linspace(0, 5 * tau, 1000)  # Simulating for 5 time constants

# Natural response equations
V_C = V0 * np.exp(-t / tau)  # Voltage across capacitor
I_R = (V0 / R) * np.exp(-t / tau)  # Current through resistor

# Create figure and 3D axis
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Initialize empty lines for animation
line_VC, = ax.plot([], [], [], 'b', label='Capacitor Voltage (V_C)')
line_IR, = ax.plot([], [], [], 'r', label='Resistor Current (I_R)')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Voltage / Current')
ax.set_zlabel('Axis')
ax.set_title('3D Animated Visualization of RC Circuit Natural Response')
ax.legend()
ax.grid()
ax.set_xlim([0, max(t)])
ax.set_ylim([0, V0])
ax.set_zlim([0, 1])

# Animation function
def update(frame):
    line_VC.set_data(t[:frame], V_C[:frame])
    line_VC.set_3d_properties(np.zeros(frame))
    
    line_IR.set_data(t[:frame], I_R[:frame])
    line_IR.set_3d_properties(np.ones(frame))
    
    return line_VC, line_IR

# Create animation
ani = animation.FuncAnimation(fig, update, frames=len(t), interval=20, blit=True)

plt.show()

