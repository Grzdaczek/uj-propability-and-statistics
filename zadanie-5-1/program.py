import numpy as np
from matplotlib import pyplot as plt

def poisson(l):
    q = np.exp(-l)
    k = 0
    s = q
    p = q
    u = np.random.uniform()
    while u > s:
        k += 1
        p *= l / k
        s += p
    return k

def poisson_dencity(l, k):
    return np.exp(-l) * (l ** k) / np.math.factorial(k)

data1 = [poisson(4) for _ in range(0, 10**2)]
data2 = [poisson(4) for _ in range(0, 10**3)]
data3 = [poisson(4) for _ in range(0, 10**5)]

r = range(1, 12)
refX = [x for x in r]
refY = [poisson_dencity(4, x) for x in r]
bins = [x - 0.5 for x in r]

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True, figsize=(10, 5))

ax1.set_title(r'$ k=10^2 $')
ax1.hist(data1, density=True, bins=bins)
ax1.plot(refX, refY, linestyle='--', marker='o')

ax2.set_title(r'$ k=10^3 $')
ax2.hist(data2, density=True, bins=bins)
ax2.plot(refX, refY, linestyle='--', marker='o')

ax3.set_title(r'$ k=10^5 $')
ax3.hist(data3, density=True, bins=bins)
ax3.plot(refX, refY, linestyle='--', marker='o')

fig.tight_layout()
fig.suptitle('Rozkład Poissona $\lambda=4$,\n porównanie teoretycznego z eksperymentalnym dla $k$ próbek')
fig.subplots_adjust(top=0.8)
fig.savefig('hist.png')