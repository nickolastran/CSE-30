
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(tight_layout = True)
ax = fig.add_subplot(1, 2, 1)
ax.set_title("Pie Plot", pad = 20)
major = ["Bio", "Chem", "Physics", "Arts", "Math"]
students = [25, 18, 45, 23, 11]
ax.pie(students, labels = major, autopct = "%1.0f%%")

ax = fig.add_subplot(1, 2, 2, polar=True)
ax.set_title("Cardioid", pad = 20)
theta = np.linspace(0, 2 * np.pi, 100)
r = 2 * (1 - np.cos(theta))
ax.plot(theta, r, color = "red")
plt.show()