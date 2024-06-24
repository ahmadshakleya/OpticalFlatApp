import numpy as np


def find_intersection_v2(shape1, shape2):
    """
    Find intersection points between a vertical cylinder and a horizontal flat surface.
    This function now accounts for variable z-values across the entire surface and checks if the
    cylinder's points are within the surface boundaries at those specific points.

    :param cylinder: Cylinder object
    :param surface: FlatSurface object
    :return: Arrays of x, y, z coordinates of intersection points
    """
    x_cyl, y_cyl, z_cyl = shape1.get_surface()
    x_surf, y_surf, z_surf = shape2.get_surface()  # Get the full surface grid

    # Initialize empty lists for intersection points
    x_intersect, y_intersect, z_intersect = [], [], []

    # Determine the bounds of the surface
    #x_min, x_max = np.min(x_surf), np.max(x_surf)
    #y_min, y_max = np.min(y_surf), np.max(y_surf)

    # Iterate over each point in the cylinder
    for i in range(x_cyl.shape[0]):
        for j in range(x_cyl.shape[1]):
            x, y, z = x_cyl[i, j], y_cyl[i, j], z_cyl[i, j]

            # Check if the cylinder's point is within the surface bounds
            #if x_min <= x <= x_max and y_min <= y <= y_max:
                # Determine the closest indices in the surface grid

            idx_x = np.argmin(np.abs(x_surf[0, :] - x))
            idx_y = np.argmin(np.abs(y_surf[:, 0] - y))

            # Check for Z-value intersection
            if np.isclose(z, z_surf[idx_y, idx_x], 0.01, 0.01):
                x_intersect.append(x)
                y_intersect.append(y)
                z_intersect.append(z)

    return np.array(x_intersect), np.array(y_intersect), np.array(z_intersect)

