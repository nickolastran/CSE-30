
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import numpy as np
import random


def update(val):
    n = slider1.val
    d = slider2.val
    r = np.cos(theta * n / d)
    # you may need to convert val into integers
    ax.cla()
    colors = ["#E0BBE4", "#957DAD", "#D291BC", "#FEC8D8", "#FFDFD3"]
    line = ax.plot(theta + (r < 0) * np.pi, np.abs(r), colors[random.randint(0, 4)], linewidth = 1)

# main
fig = plt.figure(figsize = (8, 8))

ax = fig.add_subplot(1, 1, 1, polar = True)
ax.set_title("Rose Curve", pad = 20)

n, d = 3, 9
theta = np.linspace(0, d / n * 16 * np.pi, 600)             # you may need to adjust the theta range and increase the resolution (600)
r = np.cos(theta * n / d)                                   # you may need to convert negative values of r into positive values
#line = ax.plot(theta, r, color = "red")

plt.subplots_adjust(left = 0.25, bottom = 0.25)
slider1_ax = plt.axes([0.25, 0.15, 0.65, 0.03])
slider2_ax = plt.axes([0.25, 0.1, 0.65, 0.03])
slider1 = Slider(slider1_ax, "n value", 0, 13, valinit = n, valfmt = "%i")
slider2 = Slider(slider2_ax, "d value", 1, 12, valinit = d, valfmt = "%i")
slider1.on_changed(update)
slider2.on_changed(update)

plt.show()