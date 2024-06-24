import numpy as np

class Shape3D:
    def __init__(self, x_center=0, y_center=0, z_base=0, theta=0, phi=0, color='red', alpha=0.6):
        self.x_center = x_center
        self.y_center = y_center
        self.z_base = z_base
        self.x = None
        self.y = None
        self.z = None
        self.tilt_theta=theta
        self.tilt_phi=phi
        self.color = color
        self.alpha = alpha
    
    def get_surface(self):
        """Return the x, y, z arrays for the surface of the shape."""
        return self.x, self.y, self.z
    
    def tilt(self, theta=0, phi=0):
        self.tilt_theta = theta
        self.tilt_phi = phi
        """Apply tilt by rotating around the x and y axes."""
        # Flatten the matrices and stack them vertically
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
        
        self.x, self.y, self.z = coords.reshape(3, *self.z.shape)
        return self.x, self.y, self.z
    
    def translate(self, dx=0, dy=0, dz=0):
        """Translate the shape by the specified amounts."""
        self.x += dx
        self.y += dy
        self.z += dz

    def plot(self, fig, ax):
        """Plot the shape on the specified axis."""
        ax.plot_surface(self.x, self.y, self.z, color=self.color, alpha=self.alpha)  # Semi-transparent red

    def to_dict(self):
        return {
            "type": type(self).__name__,
            "x_center": self.x_center,
            "y_center": self.y_center,
            "z_base": self.z_base,
            "theta": self.tilt_theta,
            "phi": self.tilt_phi,
            "color": self.color,
            "alpha": self.alpha
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['x_center'], data['y_center'], data['z_base'], data['theta'], data['phi'], data['color'], data['alpha'])
        # This method should be overridden in each subclass
        #pass

    def set_x(self, new_x):
        self.x = new_x
    def set_y(self, new_y):
        self.y = new_y
    def set_z(self, new_z):
        self.z = new_z