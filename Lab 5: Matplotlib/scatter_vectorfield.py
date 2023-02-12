
import numpy as np
import matplotlib.pyplot as plt
from random import randint

fig = plt.figure(tight_layout = True)

data = np.array([[i, randint(0, 100)] for i in range(100)])     # make random data
ax = fig.add_subplot(1, 2, 1)                                   # using a different approach to arrange plots
col1 = data[:,0]                                                # extract data from the 1st column
col2 = data[:,1]                                                # extract data from the 2nd column
ax.scatter(col1, col2, s = 1.5, color = "green")
ax.set_title("Scatter")
ax.set_xlabel("x")
ax.set_ylabel("y")

ax = fig.add_subplot(1, 2, 2)
ax.set_title("Vector Field")
x, y = np.meshgrid(np.arange(-2, 2, 0.2), np.arange(-2, 2, 0.2))
z = x * np.exp(-x ** 2 - y ** 2)
v, u = np.gradient(z, 0.2, .2)
ax.quiver(x, y, u, v)
plt.show()