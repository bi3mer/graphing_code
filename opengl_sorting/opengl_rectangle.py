import matplotlib
import matplotlib.pyplot as plt

rx = [-0.5, -0.5, 0.5, 0.5, -0.5]
ry = [-0.5, 0.5, 0.5, -0.5, -0.5]

x_axis_x = [0,0]
x_axis_y = [-1,1]

y_axis_x = [-1,1]
y_axis_y = [0,0]

fig, ax = plt.subplots()

ax.plot(rx, ry)
ax.plot(x_axis_x, x_axis_y, color='black')
ax.plot(y_axis_x, y_axis_y, color='black')

fig.savefig("example_opengl_rectangle.png")
plt.show()
