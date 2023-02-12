
import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits import mplot3d 
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

# hyperbolic parabolid
ax = plt.axes(projection = "3d")
x = np.linspace(-1, 1, 30)
y = np.linspace(-1, 1, 30)
X, Y = np.meshgrid(x, y)
a, b = 0.5, 1
Z = ((X * X / a) - (Y * Y / b))
ax.contour3D(X, Y, Z, 50)
ax.set_title("Hyperbolic Paraboloid", pad = 10)
plt.show()

# elliptic paraboloid
ax = plt.axes(projection = "3d")
x = np.linspace(-1, 1, 30)
y = np.linspace(-1, 1, 30)
X, Y = np.meshgrid(x, y)
a, b = 0.5, 1
Z = ((X ** 2) + (Y ** 2))
ax.contour3D(X, Y, Z, 50)
ax.set_title("Elliptic Paraboloid", pad = 10)
plt.show()


# ellipsoid
ax = plt.axes(projection = "3d")
theta = np.linspace(0, np.pi, 30).reshape(-1, 30)
phi = np.linspace(0,2 * np.pi, 30).reshape(30, 1)
X = np.sin(theta) * np.cos(phi)
Y = np.sin(theta) * np.sin(phi)
Z = np.cos(theta)
ax.plot_surface(X, Y, Z)
ax.set_title("Ellipsoid", pad = 10)
plt.show()


# cone
ax = plt.axes(projection = "3d")
u = np.linspace(-1, 1, 100)
v = np.linspace(0, 2 * np.pi, 60)
u, v = np.meshgrid(u, v)
X = ((1 - u) / 1) * np.cos(v)
Y = ((1 - u) / 1) * np.sin(v)
Z = np.sin(u)
ax.contour3D(X, Y, Z, 50)
ax.set_title("Cone", pad = 10)
plt.show()


# square pyramid
ax = plt.axes(projection = "3d")
points = np.array([
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0.5, 0.5, 1]])

X = points[ : ,0]
Y = points[ : ,1]
Z = points[ : ,2]

ax.plot_trisurf(X, Y, Z)
ax.set_title("Square Pyramid", pad = 10)
plt.show()


# parallelepiped
ax = plt.axes(projection = "3d")
points = np.array([
    [-1, -1, -1],
    [1, -1, -1 ],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, 1],
    [1, -1, 1 ],
    [1, 1, 1],
    [-1, 1, 1]])

point = [
    [2.06498904e-01, -6.30755443e-07, 1.07477548e-03],
    [1.61535574e-06, 1.18897198e-01, 7.85307721e-06],
    [7.08353661e-02, 4.48415767e-06, 2.05395893e-01]]

Z = np.zeros((8, 3))
for i in range(8): Z[i, :] = np.dot(points[i, :], point)
Z = 10.0 * Z
r = [-1,1]
X, Y = np.meshgrid(r, r)
ax.scatter3D(Z[:, 0], Z[:, 1], Z[:, 2])

vertices = [
    [Z[0],Z[1],Z[2],Z[3]],
    [Z[4],Z[5],Z[6],Z[7]], 
    [Z[0],Z[1],Z[5],Z[4]], 
    [Z[2],Z[3],Z[7],Z[6]], 
    [Z[1],Z[2],Z[6],Z[5]],
    [Z[4],Z[7],Z[3],Z[0]]]

ax.add_collection3d(Poly3DCollection(vertices))
ax.set_title("Parallelepiped", pad = 10)
plt.show()