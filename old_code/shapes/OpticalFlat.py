import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from shapes.cylinder import Cylinder
from shapes.disk import Disk
from shapes.shape3D import Shape3D

class OpticalFlat(Shape3D):
    def __init__(self, height=5, radius=2, resolution=100, num_disks=5, wavelength=700e-9, x_center=0, y_center=0, z_base=0, theta=0, phi=0, color='red', alpha=0.6):
        super().__init__(x_center=x_center, y_center=y_center, z_base=z_base, theta=theta, phi=phi, color=color,
                         alpha=alpha)
        self.height = height
        self.radius = radius
        self.resolution = resolution
        self.num_disks = num_disks
        self.wavelength = wavelength
        self.components = []

        self.create_cylinder()
        self.create_disks()

    def create_cylinder(self):
        """ Create the main cylinder of the optical flat. """
        cylinder = Cylinder(height=self.height, radius=self.radius, x_center=self.x_center,
                            y_center=self.y_center, z_base=self.z_base, resolution=self.resolution)
        self.components.append(cylinder)

    def create_disks(self):
        """ Create the base and additional disks along the cylinder's height. """
        # Base disk just below the cylinder
        base_disk = Disk(radius=self.radius, x_center=self.x_center, y_center=self.y_center,
                         z_base=self.z_base, resolution=self.resolution)
        self.components.append(base_disk)

        # Additional disks inside the cylinder, each separated by half a wavelength
        for i in range(1, self.num_disks + 1):
            disk_height = self.z_base - i * (self.wavelength / 2)  # Each disk is half a wavelength apart
            disk = Disk(radius=self.radius, x_center=self.x_center, y_center=self.y_center,
                        z_base=disk_height, resolution=self.resolution)
            self.components.append(disk)

    def tilt(self, theta=0, phi=0):
        """ Apply tilt to the optical flat by rotating around the x and y axes. """
        for component in self.components:
            component.tilt(theta, phi)
    
    def get_surface(self):
        """ Return the x, y, and z values of the optical flat's surface. """
        x, y, z = [], [], []
        for component in self.components:
            x_comp, y_comp, z_comp = component.get_surface()
            x.append(x_comp)
            y.append(y_comp)
            z.append(z_comp)
        return np.vstack(x), np.vstack(y), np.vstack(z)

    def translate(self, dx=0, dy=0, dz=0):
        """ Translate the optical flat by the specified amounts. """
        for component in self.components:
            component.translate(dx, dy, dz)

    def plot(self, fig, ax, color='r', alpha=0.6, show_cylinder=True):
        """ Plot all components of the optical flat. """
        for component in self.components:
            if isinstance(component, Cylinder) and not show_cylinder:
                continue
            x, y, z = component.get_surface()
            ax.plot_surface(x, y, z, color=color, alpha=alpha)

    def get_components(self):
        return self.components
    
    def get_cylinder(self):
        return self.components[0]

    def get_disks(self):
        return self.components[1:]

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "height": self.height,
            "radius": self.radius,
            "resolution": self.resolution,
            "num_disks": self.num_disks,
            "wavelength": self.wavelength
        })
        return data

    @classmethod
    def from_dict(cls, data):
        optical_flat = cls(data['height'], data['radius'], data['resolution'], data['num_disks'], data['wavelength'], data['x_center'], data['y_center'], data['z_base'], data['theta'], data['phi'], data['color'], data['alpha'])
        return optical_flat
