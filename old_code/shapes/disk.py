import numpy as np
import shapes.shape3D as shape3D

class Disk(shape3D.Shape3D):
    def __init__(self, radius, resolution=100, x_center=0, y_center=0, z_base=0, theta=0, phi=0, color='red', alpha=0.6):
        super().__init__(x_center=x_center, y_center=y_center, z_base=z_base, theta=theta, phi=phi, color=color, alpha=alpha)
        self.radius = radius
        self.resolution = resolution
        self.create_disk()

    def create_disk(self):
        """Generate the disk's surface."""
        theta = np.linspace(0, 2 * np.pi, self.resolution)
        r = np.linspace(0, self.radius, self.resolution)
        theta, r = np.meshgrid(theta, r)
        self.x = r * np.cos(theta) + self.x_center
        self.y = r * np.sin(theta) + self.y_center
        self.z = np.zeros_like(self.x) + self.z_base

    '''
    def rotate(self, angle, axis='z'):
        """Rotate the disk around the specified axis by the given angle in degrees."""
        angle = np.radians(angle)
        if axis == 'x':
            cos_angle = np.cos(angle)
            sin_angle = np.sin(angle)
            y_new = self.y * cos_angle - self.z * sin_angle
            z_new = self.y * sin_angle + self.z * cos_angle
            self.y, self.z = y_new, z_new
        elif axis == 'y':
            cos_angle = np.cos(angle)
            sin_angle = np.sin(angle)
            x_new = self.x * cos_angle + self.z * sin_angle
            z_new = -self.x * sin_angle + self.z * cos_angle
            self.x, self.z = x_new, z_new
        elif axis == 'z':
            cos_angle = np.cos(angle)
            sin_angle = np.sin(angle)
            x_new = self.x * cos_angle - self.y * sin_angle
            y_new = self.x * sin_angle + self.y * cos_angle
            self.x, self.y = x_new, y_new
    '''
    def get_surface(self):
        return super().get_surface()
    
    def to_dict(self):
        data = super().to_dict()
        data.update({
            "radius": self.radius,
            "resolution": self.resolution
        })
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data['radius'], data['resolution'], data['x_center'], data['y_center'], data['z_base'], data['theta'], data['phi'], data['color'], data['alpha'])

    def set_radius(self, new_radius):
        self.radius = new_radius

    def set_resolution(self, new_resolution):
        self.resolution = new_resolution