import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt('data.csv', delimiter=',')
x, y = data.T
fig = plt.figure()
ax = plt.gca()
ax.scatter(x, np.abs(y-np.pi), s=2)
ax.set_yscale('log')
ax.set_xscale('log')
plt.grid()
plt.title('Błąd wartości PI obliczonej metodą Monte Carlo dla N próbek', pad=15)
plt.ylabel('log |E|')
plt.xlabel('log N')

plt.show()