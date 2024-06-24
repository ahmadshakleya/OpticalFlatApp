import unittest

from shapes.disk import Disk
from shapes.shape3D import Shape3D
from shapes.cylinder import Cylinder

class TestSerialization(unittest.TestCase):
    def test_shape3d_serialization(self):
        # Create a Shape3D object
        shape = Shape3D(x_center=1, y_center=2, z_base=3, theta=45, phi=30, color='blue', alpha=0.8)

        # Serialize the object
        data = shape.to_dict()

        # Deserialize the data
        new_shape = Shape3D.from_dict(data)

        # Check if the attributes are equal
        self.assertEqual(new_shape.x_center, shape.x_center)
        self.assertEqual(new_shape.y_center, shape.y_center)
        self.assertEqual(new_shape.z_base, shape.z_base)
        self.assertEqual(new_shape.theta, shape.theta)
        self.assertEqual(new_shape.phi, shape.phi)
        self.assertEqual(new_shape.color, shape.color)
        self.assertEqual(new_shape.alpha, shape.alpha)

    def test_cylinder_serialization(self):
        # Create a Cylinder object
        cylinder = Cylinder(height=20, radius=2, resolution=50, x_center=5, y_center=5, z_base=5, theta=90, phi=45, color='red', alpha=0.7)

        # Serialize the object
        data = cylinder.to_dict()

        # Deserialize the data
        new_cylinder = Cylinder.from_dict(data)

        # Check if the attributes are equal
        self.assertEqual(new_cylinder.height, cylinder.height)
        self.assertEqual(new_cylinder.radius, cylinder.radius)
        self.assertEqual(new_cylinder.resolution, cylinder.resolution)
        self.assertEqual(new_cylinder.x_center, cylinder.x_center)
        self.assertEqual(new_cylinder.y_center, cylinder.y_center)
        self.assertEqual(new_cylinder.z_base, cylinder.z_base)
        self.assertEqual(new_cylinder.theta, cylinder.theta)
        self.assertEqual(new_cylinder.phi, cylinder.phi)
        self.assertEqual(new_cylinder.color, cylinder.color)
        self.assertEqual(new_cylinder.alpha, cylinder.alpha)

    def test_disk_serialization(self):
        # Create a Cylinder object
        disk = Disk(radius=2, resolution=50, x_center=5, y_center=5, z_base=5, theta=90, phi=45, color='red', alpha=0.7)

        # Serialize the object
        data = disk.to_dict()

        # Deserialize the data
        new_disk = Disk.from_dict(data)

        # Check if the attributes are equal
        self.assertEqual(new_disk.radius, disk.radius)
        self.assertEqual(new_disk.resolution, disk.resolution)
        self.assertEqual(new_disk.x_center, disk.x_center)
        self.assertEqual(new_disk.y_center, disk.y_center)
        self.assertEqual(new_disk.z_base, disk.z_base)
        self.assertEqual(new_disk.theta, disk.theta)
        self.assertEqual(new_disk.phi, disk.phi)
        self.assertEqual(new_disk.color, disk.color)
        self.assertEqual(new_disk.alpha, disk.alpha)

if __name__ == '__main__':
    unittest.main()
