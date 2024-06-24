import numpy as np
from rotate_functions import rotate_x, rotate_y

# Test the rotation
test_coords = np.array([[1, 0, 0]])  # Point along the x-axis
rotated_coords_x = rotate_x(test_coords, 90)  # Should rotate to x-axis (no change in x, z should be 0)
rotated_coords_y = rotate_y(test_coords, 90)  # Should rotate to z-axis (x should become 0, y should be 0)

print("Rotated around X:", rotated_coords_x)  # Expect [1, 0, 0]
print("Rotated around Y:", rotated_coords_y)  # Expect [0, 0, 1]


