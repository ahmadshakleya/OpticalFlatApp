import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from STLFigure import STLFigure
from disk import Disk
from flat_surface import FlatSurface
from cylinder import Cylinder
from gui_utility.intersection import find_intersection
from gui_utility.utility import refine_stl_mesh

surface = FlatSurface(x_range=(-5, 50), y_range=(-5, 50), resolution=1000, z_base=5)
x_flat, y_flat, z_flat = surface.get_surface()

#surface2 = FlatSurface(x_range=(-5, 5), y_range=(-5, 5), resolution=100, z_base=1)
#x_flat2, y_flat2, z_flat2 = surface2.get_surface()
#x_flat2, y_flat2, z_flat2 = surface2.tilt(90)

#cylinder = Cylinder(height=5, radius=2, x_center=0, y_center=0, resolution=1000)
#x_cyl, y_cyl, z_cyl = cylinder.get_surface()  # Get original coordinates

# Rotate the cylinder around the X axis by 10 degrees
#x_cyl, y_cyl, z_cyl = cylinder.tilt(theta=70)

#disk = Disk(radius=5, x_center=0, y_center=0, z_base=0, resolution=1500)
#disk.rotate(45, 'x')  # Rotate the disk 45 degrees around the x-axis

file_path, _ = refine_stl_mesh('hemisphere.stl', 4)
print(file_path)
stl_figure = STLFigure(file_path, x_center=0, y_center=0, z_base=0)
#stl_figure.tilt(90)
x_stl, y_stl, z_stl = stl_figure.get_surface()


#x_int, y_int, z_int = find_intersection(cylinder, surface)
#x_int, y_int, z_int = find_intersection(surface2, surface)
#x_int, y_int, z_int = find_intersection(disk, surface)
#x_int, y_int, z_int = find_intersection(disk, cylinder)
x_int, y_int, z_int = find_intersection(stl_figure, surface)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x_flat, y_flat, z_flat, color='b', alpha=0.2)  # Semi-transparent
# Plot the flat surface2
#ax.plot_surface(x_flat2, y_flat2, z_flat2, color='b', alpha=0.5)  # Semi-transparent

# Plot the rotated cylinder
#ax.plot_surface(x_cyl, y_cyl, z_cyl, color='r', alpha=0.6)  # Semi-transparent red

# Plot the rotated disk
#ax.plot_surface(disk.x, disk.y, disk.z, color='g', alpha=0.6)  # Semi-transparent green

ax.plot_surface(x_stl, y_stl, z_stl, color='r', alpha=0.6)  # Semi-transparent red

# Plot the intersection points
if x_int.size > 0 and y_int.size > 0 and z_int.size > 0:
    ax.scatter(x_int, y_int, z_int, color='black', s=50)

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Shapes: Flat Surface and Rotated Cylinder')

plt.show()