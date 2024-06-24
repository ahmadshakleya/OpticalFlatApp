import math
import numpy as np
from stl import mesh
import os
import shapes.shape3D as shape3D
from gui_utility.utility import rotate_x, rotate_y
from gui_utility.utility import refine_stl_mesh

class STLFigure(shape3D.Shape3D):
    def __init__(self, file_path, x_center=0, y_center=0, z_base=0, theta=0, phi=0, color='red', alpha=0.6):
        super().__init__(x_center=x_center, y_center=y_center, z_base=z_base, theta=theta, phi=phi, color=color, alpha=alpha)
        self.file_path = file_path
        self.load_stl()

    def load_stl(self):
        """Load and process the STL file."""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"The file {self.file_path} does not exist")
        self.mesh = mesh.Mesh.from_file(self.file_path)

        # Convert vertices to numpy arrays and adjust for initial positioning
        self.x = self.mesh.vectors[:,:,0] + self.x_center
        self.y = self.mesh.vectors[:,:,1] + self.y_center
        self.z = self.mesh.vectors[:,:,2] + self.z_base

    def translate(self, dx=0, dy=0, dz=0):
        """Translate the STL figure."""
        self.x += dx
        self.y += dy
        self.z += dz

    def tilt(self, theta=0, phi=0):
        """Apply tilt by rotating around the x and y axes."""
        self.tilt_theta = theta
        self.tilt_phi = phi
        # Flatten the matrices and stack them vertically for rotation
        coords = np.vstack((self.x.flatten(), self.y.flatten(), self.z.flatten()))

        # Rotate around the X-axis
        if theta != 0:
            coords = rotate_x(coords.T, theta).T
        # Rotate around the Y-axis
        if phi != 0:
            coords = rotate_y(coords.T, phi).T

        # Reshape the coordinates back to their original shape
        self.x, self.y, self.z = coords.reshape(3, *self.x.shape)

    def get_surface(self):
        """
        Returns the x, y, and z values of the STL figure.
        """
        return self.x, self.y, self.z

    def to_dict(self):
        data = super().to_dict()
        data['file_path'] = self.file_path
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data['file_path'], data['x_center'], data['y_center'], data['z_base'], data['theta'], data['phi'], data['color'], data['alpha'])
