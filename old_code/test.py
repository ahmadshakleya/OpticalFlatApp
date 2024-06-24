import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import KDTree
from disk import Disk
from cylinder import Cylinder
from gui_utility.intersection import find_intersection
import numpy as np

cylinder = Cylinder(height=5, radius=2, x_center=0, y_center=0, resolution=1000)
x_cyl, y_cyl, z_cyl = cylinder.tilt(theta=70)

disk = Disk(radius=5, x_center=0, y_center=0, z_base=0, resolution=1500)
disk.rotate(45, 'x')

x_int, y_int, z_int = find_intersection(disk, cylinder)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x_cyl, y_cyl, z_cyl, color='r', alpha=0.6)

ax.plot_surface(disk.x, disk.y, disk.z, color='g', alpha=0.6)

if x_int.size > 0 and y_int.size > 0 and z_int.size > 0:
    ax.scatter(x_int, y_int, z_int, color='black', s=10)  # Black dots for intersection
    # Build a k-d tree from the intersection points
    points = np.vstack((x_int, y_int, z_int)).T
    tree = KDTree(points)
    # For each point, find its nearest neighbor and draw a line
    for point in points:
        distances, indices = tree.query(point, k=2)  # k=2 to find the nearest and itself
        nearest_point = points[indices[1]]  # indices[1] because indices[0] is the point itself
        ax.plot([point[0], nearest_point[0]], [point[1], nearest_point[1]], [point[2], nearest_point[2]], 'k-')

# Labels and title
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Intersection between a Cylinder and a Disk')

# Show the plot
plt.show()
