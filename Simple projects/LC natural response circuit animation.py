import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define circuit parameters
L = 10e-3  # Inductance in Henry (10mH)
C = 10e-6  # Capacitance in Farads (10µF)
Q0 = 1e-6  # Initial charge on capacitor (1µC)

# Compute natural frequency
omega = 1 / np.sqrt(L * C)
T = 2 * np.pi / omega  # Time period of oscillation

# Time setup
t = np.linspace(0, 5 * T, 1000)  # Simulate for 5 periods

# Compute charge, voltage, and current
q_t = Q0 * np.cos(omega * t)  # Charge on capacitor
v_c = q_t / C  # Voltage across capacitor
i_L = -Q0 * omega * np.sin(omega * t)  # Current through inductor

# Create figure
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(0, max(t))
ax.set_ylim(-max(v_c), max(v_c))
ax.set_xlabel('Time (s)')
ax.set_ylabel('Voltage / Current')
ax.set_title('Natural Response of LC Circuit')
ax.grid()

# Initialize plots
line_vc, = ax.plot([], [], 'b', label='Capacitor Voltage (V_C)')
line_il, = ax.plot([], [], 'r', label='Inductor Current (I_L)')
ax.legend()

# Animation function
def update(frame):
    line_vc.set_data(t[:frame], v_c[:frame])
    line_il.set_data(t[:frame], i_L[:frame])
    return line_vc, line_il

# Create animation
ani = animation.FuncAnimation(fig, update, frames=len(t), interval=20, blit=True)

plt.show()
