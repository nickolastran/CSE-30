
import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits import mplot3d 
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection


def pyramid(x, y):
    a, b  = np.mgrid[0 : x : 1, 0 : y : 1]
    X = a * np.cos(b)
    Y = a * np.sin(b)
    Z = np.sqrt(X ** 2 + Y ** 2)
    ax.invert_zaxis()
    return X, Y, Z

if __name__ == "__main__":
    fig = plt.figure(tight_layout = True)
    ax = fig.add_subplot(121, projection = "3d")
    x, y, z = pyramid(4, 5)
    ax.contour3D(x, y, z, 50)
    ax = fig.add_subplot(122, projection = "3d")
    x, y, z = pyramid(6, 10)
    ax.contour3D(x, y, z, 50)
    plt.show()
