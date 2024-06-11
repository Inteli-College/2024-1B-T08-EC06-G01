import numpy as np
import matplotlib.pyplot as plt


radius = 10
center = (0, 0)
resolution = 100
x = np.linspace(-radius, radius, resolution)
y = np.linspace(-radius, radius, resolution)
X, Y = np.meshgrid(x, y)
Z = np.sqrt(X**2 + Y**2) 

plt.figure(figsize=(6, 6))
plt.imshow(Z, cmap='hot', extent=[-radius, radius, -radius, radius])
plt.colorbar()
plt.title('Heatmap')
plt.show()
