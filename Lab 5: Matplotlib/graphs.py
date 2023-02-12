
import numpy as np
import matplotlib.pyplot as plt
import random

trials = []
results = []
for i in range(100):
    trials.append(i)
    results.append(random.randint(1, 6) + random.randint(1, 6))

rolls = {}
for i in results:
    try:
        rolls[i] += 1
    except:
        rolls[i] = 1
rolls = dict(sorted(rolls.items()))


graphs = plt.figure(tight_layout = True)

ax = graphs.add_subplot(2, 2, 1)
ax.set_title("Histogram")
ax.hist(results, bins = 11)

ax = graphs.add_subplot(2, 2, 2)
ax.set_title("Scatter")
ax.scatter(trials, results)

ax = graphs.add_subplot(2, 2, 3)
ax.set_title("Line")
ax.plot(trials, results)

ax = graphs.add_subplot(2, 2, 4)
ax.set_title("Pie")
ax.pie(list(rolls.values()), labels = list(rolls.keys()))
plt.show()