import numpy as np
import matplotlib.pyplot as plt

# create array with 400 floats, evenly spaced
t = np.arange(0, 0.5, 0.005)

print("t lengfth", len(t))

#one different oscillaiton patterns, cahnnel 9(UWB standard) is 8ghz
a = np.cos(2*np.pi*8.0*t)
b = np.cos(2*np.pi*8.5*t)

plt.plot(t, a, marker='.')
plt.plot(t, b, marker='o')

plt.show()
