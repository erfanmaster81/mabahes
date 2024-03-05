import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,2*np.pi,.01)
y1 = np.sin (x)
y2 = np.cos (x)


plt.grid()
plt.plot(x,y1)
plt.plot(x,y2)
plt.fill_between(x,y1,y2,hatch='//',color='gray',fc='white')
plt.show()

