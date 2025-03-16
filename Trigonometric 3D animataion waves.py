import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Create a figure and axis for 3D plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Set the x-axis range from 0 to 360 degrees and generate points
x = np.linspace(0, 360, 1000)  # Angle values in degrees

# Y values for sine and cosine (we will display these in two rows)
Y_sin = np.zeros_like(x)  # Y = 0 for sine wave
Y_cos = np.ones_like(x)   # Y = 1 for cosine wave

# Initial Z values for sine and cosine waves (sine and cosine values)
Z_sin = np.sin(np.radians(x))
Z_cos = np.cos(np.radians(x))

# Plot initial sine and cosine as lines
line_sin, = ax.plot(x, Y_sin, Z_sin, color='blue', label='sin(x)')
line_cos, = ax.plot(x, Y_cos, Z_cos, color='red', label='cos(x)')

# Set axis labels
ax.set_xlabel('Degrees (x)')
ax.set_ylabel('Functions')
ax.set_zlabel('Amplitude (y)')
ax.set_title('3D Sine and Cosine Wave Animation')

# Set axis limits
ax.set_xlim(0, 360)
ax.set_ylim(-0.5, 1.5)  # We have two functions: sin (Y=0) and cos (Y=1)
ax.set_zlim(-1, 1)  # The sine and cosine waves oscillate between -1 and 1

# Adjust view angle to make Y-axis appear on the left (without affecting wave movement)
ax.view_init(elev=30, azim=-90)  # Elevation of 30 degrees and Azimuth of -90 degrees

# Set the x-axis ticks to be at 0, 90, 180, 270, and 360 degrees
ax.set_xticks([0, 90, 180, 270, 360])  # Manually set x-axis ticks

# Display the legend for sine and cosine
ax.legend()

# Animation function to update the sine and cosine lines
def animate(i):
    # Update sine and cosine waves as functions of x and time (i)
    Z_sin = np.sin(np.radians(x + i))  # Sine wave
    Z_cos = np.cos(np.radians(x + i))  # Cosine wave
    
    # Update the data for sine and cosine lines
    line_sin.set_data(x, Y_sin)  # X data for sine
    line_sin.set_3d_properties(Z_sin)  # Z data for sine
    
    line_cos.set_data(x, Y_cos)  # X data for cosine
    line_cos.set_3d_properties(Z_cos)  # Z data for cosine
    
    return line_sin, line_cos  # Return the updated lines

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=360, interval=20, blit=False)

# Show the animation
plt.show()
