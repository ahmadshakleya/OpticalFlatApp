import numpy as np
#from gui_utility.utility import rotate_x, rotate_y
import shapes.shape3D as shape3D

class FlatSurface(shape3D.Shape3D):
    def __init__(self, x_range=(-5, 5), y_range=(-5, 5), resolution=100, x_center=0, y_center=0, z_base=0, theta=0, phi=0, color='red', alpha=0.6):
        super().__init__(x_center=x_center, y_center=y_center, z_base=z_base, theta=theta, phi=phi, color=color, alpha=alpha)
        self.resolution = resolution
        self.x_range = x_range
        self.y_range = y_range
        self.x, self.y = np.meshgrid(
            np.linspace(x_range[0], x_range[1], self.resolution),
            np.linspace(y_range[0], y_range[1], self.resolution)
        )
        self.z = np.zeros_like(self.x) + self.z_base  # Set all z to the specified initial value
    
    
    # def tilt(self, theta=0, phi=0):
    #     """ Apply tilt by rotating around the x and y axes. """
    #     self.tilt_theta = theta
    #     self.tilt_phi = phi
    #     coords = np.vstack((self.x.flatten(), self.y.flatten(), self.z.flatten()))
    #     if theta != 0:
    #         coords = rotate_x(coords.T, theta).T
    #     if phi != 0:
    #         coords = rotate_y(coords.T, phi).T
    #     self.x, self.y, self.z = coords.reshape(3, *self.x.shape)
    #     return self.x, self.y, self.z

    def get_surface(self):
        """
        Returns the x, y, and z values of the surface.
        """
        return self.x, self.y, self.z
    
    def to_dict(self):
        data = super().to_dict()
        data.update({
            "x_range": self.x_range,
            "y_range": self.y_range,
            "resolution": self.resolution,
        })
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data['x_range'], data['y_range'], data['resolution'], data['x_center'], data['y_center'], data['z_base'], data['theta'], data['phi'], data['color'], data['alpha'])

    def set_resolution(self, new_resolution):
        self.resolution = new_resolution

    def set_x_range(self, new_x_range):
        self.x_range = new_x_range

    def set_y_range(self, new_y_range):
        self.y_range = new_y_range

    def set_z_value(self, new_z_value):
        self.z = new_z_value