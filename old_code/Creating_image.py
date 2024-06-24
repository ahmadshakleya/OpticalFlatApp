import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from shapes.OpticalFlat import OpticalFlat
from shapes.STLFigure import STLFigure
from shapes.disk import Disk
from shapes.flat_surface import FlatSurface
from shapes.cylinder import Cylinder
from gui_utility.intersection import find_intersection
from gui_utility.utility import refine_stl_mesh
import numpy as np

optical_flat = OpticalFlat(height=2, radius=10, x_center=0, y_center=0, z_base=0, resolution=100, num_disks=10, wavelength=2)
optical_flat.tilt(theta=40, phi=0)
optical_flat.translate(dy=-25)

cylinder_center = optical_flat.get_cylinder().get_center()

cylinder = Cylinder(height=10, radius=2, x_center=0, y_center=0, z_base=np.min(optical_flat.get_cylinder().get_surface()[2]), resolution=100)
cylinder.translate(dz=-30)
cylinder.tilt(theta=90, phi=0)

x_int, y_int, z_int = np.array([]), np.array([]), np.array([])
for comp in optical_flat.components:
    if not isinstance(comp, Cylinder):
        x_int_comp, y_int_comp, z_int_comp = find_intersection(comp, cylinder)
        above_xy_plane = z_int_comp > 0
        x_int = np.append(x_int, x_int_comp[above_xy_plane])
        y_int = np.append(y_int, y_int_comp[above_xy_plane])
        z_int = np.append(z_int, z_int_comp[above_xy_plane])

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

if x_int.size > 0 and y_int.size > 0 and z_int.size > 0:
    ax.scatter(x_int, y_int, z_int, color='black', s=10)

ax.scatter(*cylinder_center, color='red', s=40) 

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Optical Flat Visualization')
ax.grid(False)
ax._axis3don = False

ax.view_init(elev=90, azim=0)

plt.savefig("old_code/optical_flat_visualization2.png", dpi=300, bbox_inches='tight', pad_inches=0.1)
plt.close()
