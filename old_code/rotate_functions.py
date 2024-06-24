import numpy as np

def rotate_x(coordinates, theta):
    """ Rotate coordinates around the x-axis by theta degrees. """
    theta = np.radians(theta) 
    rotation_matrix = np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta), np.cos(theta)]
    ])
    return np.dot(coordinates, rotation_matrix)

def rotate_y(coordinates, phi):
    """ Rotate coordinates around the y-axis by phi degrees. """
    phi = np.radians(phi)
    rotation_matrix = np.array([
        [np.cos(phi), 0, np.sin(phi)],
        [0, 1, 0],
        [-np.sin(phi), 0, np.cos(phi)]
    ])
    return np.dot(coordinates, rotation_matrix)
