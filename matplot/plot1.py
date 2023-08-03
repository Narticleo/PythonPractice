import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10 ,100)
y1 = 20*(x**2) + 4
y2 = x**3 + 500
plt.figure(num = 2 , figsize = (10, 15))
plt.plot(x, y1, lw = 2 , ls = "--", c = "blue")
plt.scatter(x, y2, c = "green")
plt.xlim = (-500 , 500)
plt.ylim = (-1000, 1000)
a, b  = [-1000, 0 ,1000], ['low', 'medium', 'high']
plt.yticks(a, b)
plt.show()

