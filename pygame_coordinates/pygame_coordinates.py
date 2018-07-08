
import matplotlib.pyplot as plt
import numpy as np

# screen
x = [0, 0, 1, 1, 0]
y = [0, 1, 1, 0, 0]
plt.plot(x, y, 'k')

# corners
x = [0, 0, 1, 1]
y = [0, 1, 1, 0]
plt.scatter(x, y)

# labels
plt.text(0.02, 0.02, r'(0,0)')
plt.text(0.02, 0.94, r'(0, height)')
plt.text(0.83, 0.02, r'(width,0)')
plt.text(0.75, 0.94, r'(width, height)')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Pygame coordinates')
plt.grid(True)
plt.savefig("matplotlib_coordinates.png")
plt.show()