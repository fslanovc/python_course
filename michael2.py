import numpy as np
import matplotlib.pyplot as plt
import addcopyfighandler

xs = np.linspace(0,10*np.pi,100)
ys = np.sin(xs)
plt.plot(xs,ys)
plt.show()
#comment