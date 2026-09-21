import numpy as np
import matplotlib.pyplot as plt

# create array with 400 floats, evenly spaced
t = np.arange(-1, 3, 0.05)
t0 = 1

# create sigma to define the width of pulse
sigma = 0.425
sigma2 = 1.55e-9

#define the shape of the curve. use t for
y = np.exp( -(((t-t0)/sigma)**2) / 2 )
y2 = np.exp( -((t/sigma2)**2) / 2 )


plt.plot(t, y, marker='.')
plt.ylabel("amplitude")
plt.xlabel("time")

#plt.plot(t, y2, marker='.')
plt.ylabel("amplitude")
plt.xlabel("time")

plt.show()
