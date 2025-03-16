import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define parameters
f = 10  # Frequency in Hz
T = 1  # Duration in seconds
fs = 1000  # Sampling rate
t = np.linspace(0, T, fs * T)  # Time vector

# Compute sine wave using Euler's formula
theta = 2 * np.pi * f * t
euler_wave = np.exp(1j * theta)  # e^(jθ)
sin_wave = np.imag(euler_wave)   # Extract imaginary part
cos_wave = np.real(euler_wave)   # Extract real part

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(0, T)
ax.set_ylim(-1.2, 1.2)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Amplitude')
ax.set_title('Animated Sine and Cosine Waves Using Euler’s Formula')
ax.grid()

# Initialize the lines
line_sin, = ax.plot([], [], 'b', label='Euler Sin Wave')
line_cos, = ax.plot([], [], 'r', label='Euler Cos Wave')
ax.legend()

# Animation function
def update(frame):
    line_sin.set_data(t[:frame], sin_wave[:frame])
    line_cos.set_data(t[:frame], cos_wave[:frame])
    return line_sin, line_cos

# Create animation
ani = animation.FuncAnimation(fig, update, frames=len(t), interval=20, blit=True)

plt.show()
