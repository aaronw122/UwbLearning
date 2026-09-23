import numpy as np
import matplotlib.pyplot as plt

# create array with 400 floats, evenly spaced
t = np.arange(-1, 3, 0.05)
t0 = 1

# create sigma to define the width of pulse
sigma = 0.425

#define the shape of the curve. use t for
y = np.exp( -(((t-t0)/sigma)**2) / 2 )



plt.plot(t, y, marker='.')
plt.ylabel("amplitude")
plt.xlabel("time (ns)")
plt.axis((-1, 3, 0, 2))
#plt.plot(t, y2, marker='.')
plt.show()
