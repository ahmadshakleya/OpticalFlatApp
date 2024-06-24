import unittest
import numpy as np
import flat_surface

# Assuming FlatSurface and rotate_functions are defined elsewhere and imported correctly
class TestFlatSurface(unittest.TestCase):
    
    def setUp(self):
        self.surface = flat_surface.FlatSurface(x_range=(-5, 5), y_range=(-5, 5), resolution=10, z_base=0)
        self.x_orig, self.y_orig, self.z_orig = self.surface.get_surface()
        
    def test_initial_surface(self):
        """Test that the initial surface is flat and at the correct z-value."""
        self.assertTrue(np.all(self.z_orig == 1))
    
    def test_no_rotation(self):
        """Test that no rotation leaves the surface unchanged."""
        x, y, z = self.surface.get_surface()
        np.testing.assert_array_equal(x, self.x_orig)
        np.testing.assert_array_equal(y, self.y_orig)
        np.testing.assert_array_equal(z, self.z_orig)
        
    def test_x_rotation(self):
        """Test rotation around the x-axis."""
        x, y, z = self.surface.tilt(theta=90, phi=0)
        # Check dimensions
        self.assertEqual(x.shape, self.x_orig.shape)
        # Check z changes as expected, y should be mostly unchanged
        self.assertTrue(np.allclose(y, self.y_orig, atol=1e-5))
        # As it's rotated 90 degrees around X, z should change to what y was
        self.assertTrue(np.allclose(z, 0, atol=1e-5))
    
    def test_y_rotation(self):
        """Test rotation around the y-axis."""
        x, y, z = self.surface.tilt(theta=0, phi=90)
        # Check dimensions
        self.assertEqual(x.shape, self.x_orig.shape)
        # Check x changes as expected, z should be zero due to rotation
        self.assertTrue(np.allclose(z, 0, atol=1e-5))

    def test_combined_rotation(self):
        """Test combined rotations around x and y axes."""
        x, y, z = self.surface.tilt(theta=90, phi=90)
        self.assertEqual(x.shape, self.x_orig.shape)
        # Check behavior when both rotations are applied
        self.assertTrue(np.allclose(z, 0, atol=1e-5))

if __name__ == "__main__":
    unittest.main()
