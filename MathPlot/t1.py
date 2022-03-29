import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
ax.set_title("Can nang va Chieu cao")
ax.set_xlabel("Chieu cao(cm)")
ax.set_xlim(100, 200)
ax.set_ylabel("Can nang(kg)")
ax.set_ylim(30, 100)
heights = np.random.normal(170, 15, 100)
weights = np.random.normal(60, 10, 100)
ax.scatter(heights, weights, marker="*")
plt.show()