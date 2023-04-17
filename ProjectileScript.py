import matplotlib.pyplot as plt
import numpy as np

v0 = float(input("enter the initial velocity in m/s"))
launchAngle = float(input("enter the launch angle in degrees"))

launchAngle = np.deg2rad(launchAngle)

# the initial conditions of the simulator
g = 9.81

time_of_flight = 2.0 * v0 * np.sin(launchAngle) / g
t = np.linspace(0, time_of_flight, 1000)

x_val = v0 * np.cos(launchAngle) * t
y_val = v0 * np.sin(launchAngle) * t - 0.5 * g * t ** 2

# plot creation

fig, ax = plt.subplots()
ax.plot(x_val, y_val)
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')


plt.show()
