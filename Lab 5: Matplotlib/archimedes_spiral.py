
# Archimedes Spiral in 3D
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d        # in this code it is not required

ax = plt.axes(projection = "3d")        # create a 3D Cartesian coordinate system
z = np.linspace(0, 1, 100)              # make an array of 100 real numbers from 0 to 1 and assign them to z coords
x = z * np.sin(30 * z)                  # make a parallel array of x coords 
y = z * np.cos(30 * z)                  # make a parallel array of y coords
ax.plot3D(x, y, z, "green")
ax.set_title("Archimedes Spiral in 3D", pad = 10)
plt.show()