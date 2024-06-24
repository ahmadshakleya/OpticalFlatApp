import numpy as np
import shapes.shape3D as shape3D

class Cylinder(shape3D.Shape3D):
    def __init__(self, height=10, radius=1, resolution=100, x_center=0, y_center=0, z_base=0, theta=0, phi=0, color='red', alpha=0.6):
        """
        Initialize the cylinder with specified height, radius, and center position.
        :param height: The height of the cylinder.
        :param radius: The radius of the cylinder.
        :param x_center: The x-coordinate of the cylinder's center.
        :param y_center: The y-coordinate of the cylinder's center.
        :param z_base: The z-coordinate of the cylinder's base.
        :param resolution: Resolution of the mesh for the cylinder.
        :param kwargs: Keyword arguments to be passed to the parent class.
        """
        super().__init__(x_center=x_center, y_center=y_center, z_base=z_base, theta=theta, phi=phi, color=color, alpha=alpha)

        self.height = height
        self.radius = radius
        self.resolution = resolution

        theta = np.linspace(0, 2*np.pi, resolution)
        z = np.linspace(0, height, resolution) + self.z_base  # Start Z from z_base instead of 0
        theta_grid, z_grid = np.meshgrid(theta, z)  # Create meshgrid for theta and z
        self.x = radius * np.cos(theta_grid) + self.x_center
        self.y = radius * np.sin(theta_grid) + self.y_center
        self.z = z_grid  # Direct use of meshgrid output for z


    
    def tilt(self, theta=0, phi=0):
        """ Apply tilt by rotating around the x and y axes. """
        # Flatten the matrices and stack them vertically
        self.tilt_theta = theta
        self.tilt_phi = phi
        coords = np.vstack((self.x.flatten(), self.y.flatten(), self.z.flatten()))
        
        # Rotation around the X-axis
        if theta != 0:
            rotation_matrix = np.array([
                [1, 0, 0],
                [0, np.cos(np.radians(theta)), -np.sin(np.radians(theta))],
                [0, np.sin(np.radians(theta)), np.cos(np.radians(theta))]
            ])
            coords = coords.T @ rotation_matrix
            coords = coords.T
        
        # Rotation around the Y-axis
        if phi != 0:
            rotation_matrix = np.array([
                [np.cos(np.radians(phi)), 0, np.sin(np.radians(phi))],
                [0, 1, 0],
                [-np.sin(np.radians(phi)), 0, np.cos(np.radians(phi))]
            ])
            coords = coords.T @ rotation_matrix
            coords = coords.T
        
        self.x, self.y, self.z = coords.reshape(3, *self.z.shape)  # Reshape back to original dimensions
        return self.x, self.y, self.z
    
    def get_surface(self):
        """
        Returns the x, y, and z values of the cylinder's surface.
        """
        return self.x, self.y, self.z
    
    def to_dict(self):
        data = super().to_dict()
        data.update({
            "height": self.height,
            "radius": self.radius,
            "resolution": self.resolution
        })
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data['height'], data['radius'], data['resolution'], data['x_center'], data['y_center'], data['z_base'], data['theta'], data['phi'], data['color'], data['alpha'])
    
    def get_center(self):
        # This function calculates the center of the cylinder after translation and rotation:
        x_center = np.mean(self.x)
        y_center = np.mean(self.y)
        z_center = np.mean(self.z)
        return x_center, y_center, z_center

    def set_height(self, new_height):
        self.height = new_height

    def set_radius(self, new_radius):
        self.radius = new_radius

    def set_resolution(self, new_resolution):
        self.resolution = new_resolution