
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 10)
# subplot arranges plots at different positions in the window
# arguments 2, 2, 1 mean 2x2 matrix (4 positions) at the first position
plt.subplot(2, 2, 1) 
plt.plot(x, x * x, c = "green")
plt.title("Square")
# arguments 2, 2, 2 mean 2x2 matrix (4 positions) at the second position
plt.subplot(2, 2, 2)
plt.plot(x, np.sqrt(x), c = "red")
plt.title("Square root")
# arguments 2, 2, 3 mean 2x2 matrix (4 positions) at the third position
plt.subplot(2, 2, 3)
plt.plot(x, np.exp(x), c = "orange")
plt.title("Exp")
# arguments 2, 2, 4 mean 2x2 matrix (4 positions) at the fourth position
plt.subplot(2, 2, 4)
plt.plot(x, np.log10(x), c = "blue")
plt.title("Log")
plt.show()