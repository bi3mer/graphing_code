import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def draw_cube(size, color):
	# create edges
    point_1 = (-size,-size,-size)
    point_2 = (size,-size,-size)
    point_3 = (size,size,-size)
    point_4 = (-size,size,-size)
    point_5 = (-size,-size,size)
    point_6 = (size,-size,size)
    point_7 = (size,size,size)
    point_8 = (-size,size,size)

    edges = [(point_1, point_2, point_3, point_4),
             (point_5, point_6, point_7, point_8),
             (point_2, point_3, point_7, point_6),
             (point_3, point_4, point_8, point_7),
             (point_1, point_4, point_8, point_5),
             (point_1, point_5, point_6, point_2)]
    
    # draw cube
    faces = Poly3DCollection(edges, linewidths=1, edgecolors='k')
    faces.set_facecolor(color)

    ax.add_collection3d(faces)
    ax.set_aspect('equal')

draw_cube(1, (1,0,0,1))
draw_cube(2, (0.8,0,0.8,0.5))
draw_cube(3, (0,0.8,0,0.1))

plt.show()