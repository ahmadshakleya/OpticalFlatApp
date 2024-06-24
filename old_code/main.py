import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from OpticalFlat import OpticalFlat
from STLFigure import STLFigure
from disk import Disk
from flat_surface import FlatSurface
from cylinder import Cylinder
from gui_utility.intersection import find_intersection
from gui_utility.utility import refine_stl_mesh
import numpy as np

optical_flat = OpticalFlat(height=2, radius=10, x_center=0, y_center=0, z_base=0, resolution=500, num_disks=4)
#optical_flat.translate(dz=-20)
optical_flat.tilt(theta=40, phi=0)
optical_flat.translate(dy=-25)

x_cyl, y_cyl, z_cyl = optical_flat.get_cylinder().get_surface()

z_min = np.min(z_cyl)

#flat_surface = FlatSurface(x_range=(-5, 5), y_range=(-5, 5), resolution=100, z_value=z_min)
cylinder = Cylinder(height=10, radius=2, x_center=0, y_center=0, z_base=z_min, resolution=500)
cylinder.translate(dz=-30)
cylinder.tilt(theta=90, phi=0)

#file_path = 'hemisphere.stl'
#file_path, _ = refine_stl_mesh('hemisphere.stl', 4)
#stl_figure = STLFigure(file_path, x_center=0, y_center=0, z_base=0)
#stl_figure.translate(0, -20, -20)

""" x_int, y_int, z_int = np.array([]), np.array([]), np.array([])
for comp in optical_flat.components:
    if not isinstance(comp, Cylinder):
        #x_int_comp, y_int_comp, z_int_comp = find_intersection(comp, flat_surface)
        x_int_comp, y_int_comp, z_int_comp = find_intersection(comp, cylinder)
        #x_int_comp, y_int_comp, z_int_comp = find_intersection(comp, stl_figure)
        x_int = np.append(x_int, x_int_comp)
        y_int = np.append(y_int, y_int_comp)
        z_int = np.append(z_int, z_int_comp) """

x_int, y_int, z_int = np.array([]), np.array([]), np.array([])
for comp in optical_flat.components:
    if not isinstance(comp, Cylinder):
        x_int_comp, y_int_comp, z_int_comp = find_intersection(comp, cylinder)
        above_xy_plane = z_int_comp > 0 
        x_int = np.append(x_int, x_int_comp[above_xy_plane])
        y_int = np.append(y_int, y_int_comp[above_xy_plane])
        z_int = np.append(z_int, z_int_comp[above_xy_plane])


print(x_int, y_int, z_int)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

if x_int.size > 0 and y_int.size > 0 and z_int.size > 0:
    ax.scatter(x_int, y_int, z_int, color='black', s=10) 

#optical_flat.plot(fig, ax, color='g', alpha=0.2, show_cylinder=False)
#flat_surface.plot(fig, ax)
#cylinder.plot(fig, ax, alpha=100.0)
#stl_figure.plot(fig, ax, color='r', alpha=0.6)


ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Optical Flat Visualization')
ax.view_init(elev=90, azim=0)

plt.show()