import matplotlib.pyplot as plt
import numpy as np

def F_inverse(x):
	# 0<=x<=1
	if x < 1/6:
		return np.sqrt(6*x) - 1
	elif x < 5/6:
		return 3*x - 1/2
	else:
		return 3 - np.sqrt(6 - 6*x)

dataset1 = [F_inverse(np.random.uniform()) for _ in range(0, 10**3)]
dataset2 = [F_inverse(np.random.uniform()) for _ in range(0, 10**4)]
dataset3 = [F_inverse(np.random.uniform()) for _ in range(0, 10**5)]
referenceX = [-1, 0, 2, 3]
referenceY = [0, 1/3, 1/3, 0]

fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
fig.tight_layout(pad=2.0)

params = {
	'bins': 100,
	'density': True,
	'facecolor': '#19c0ff',
	'edgecolor': '#02a0cf',
	'linewidth': 0.5
}

ax1.set_title('dla 1,000 losowań')
ax1.hist(dataset1, **params)
ax1.plot(referenceX, referenceY)

ax2.set_title('dla 10,000 losowań')
ax2.hist(dataset2, **params)
ax2.plot(referenceX, referenceY)

ax3.set_title('dla 100,000 losowań')
ax3.hist(dataset3, **params)
ax3.plot(referenceX, referenceY)

plt.show()