import json
import numpy as np
from stl import mesh

from shapes.cylinder import Cylinder
from shapes.disk import Disk
from shapes.flat_surface import FlatSurface
#from shapes.OpticalFlat import OpticalFlat
#from shapes.STLFigure import STLFigure
from shapes.shape3D import Shape3D

def interpolate_points(p1, p2):
        return (p1 + p2) / 2

def refine_stl_mesh(stl_path, resolution):
    your_mesh = mesh.Mesh.from_file(stl_path)
    new_data = np.zeros(len(your_mesh.data) * resolution, dtype=mesh.Mesh.dtype)
    
    for i, f in enumerate(your_mesh.data):
        v0, v1, v2 = f['vectors']
        v01 = interpolate_points(v0, v1)
        v12 = interpolate_points(v1, v2)
        v20 = interpolate_points(v2, v0)
        idx = i * 4
        new_data['vectors'][idx] = np.array([v0, v01, v20])
        new_data['vectors'][idx + 1] = np.array([v01, v1, v12])
        new_data['vectors'][idx + 2] = np.array([v01, v12, v20])
        new_data['vectors'][idx + 3] = np.array([v20, v12, v2])

    new_mesh = mesh.Mesh(new_data)
    stl_path = stl_path.split('.')[0] + '_refined.stl'
    new_mesh.save(stl_path)
    
    return stl_path, new_mesh

def export_shapes(shapes, filename):
    with open(filename, 'w') as f:
        json.dump([shape.to_dict() for shape in shapes], f, indent=4)

def import_shapes(filename):
    with open(filename, 'r') as f:
        shapes_data = json.load(f)
        print(shapes_data)
    shapes = []
    for shape_data in shapes_data:
        shape_type = shape_data['type']
        if shape_type == 'Cylinder':
            shape = Cylinder.from_dict(shape_data)
        elif shape_type == 'Disk':
            shape = Disk.from_dict(shape_data)
        elif shape_type == 'FlatSurface':
            shape = FlatSurface.from_dict(shape_data)
        shapes.append([shape, shape_data['id']])
    return shapes

import numpy as np

def make_circle(points):
    shuffled = points[:]
    np.random.shuffle(shuffled)
    circle = None
    for (i, p) in enumerate(shuffled):
        if circle is None or not is_in_circle(circle, p):
            circle = _make_circle_one_point(shuffled[:i + 1], p)
    return circle

def is_in_circle(circle, point):
    if circle is None:
        return False
    x, y, r = circle
    dx = x - point[0]
    dy = y - point[1]
    return dx * dx + dy * dy <= r * r + 1e-12

def _make_circle_one_point(points, p):
    circle = (p[0], p[1], 0.0)
    for (i, q) in enumerate(points):
        if not is_in_circle(circle, q):
            if circle[2] == 0.0:
                circle = make_diameter(p, q)
            else:
                circle = _make_circle_two_points(points[:i + 1], p, q)
    return circle

def make_diameter(p1, p2):
    cx = (p1[0] + p2[0]) / 2
    cy = (p1[1] + p2[1]) / 2
    r0 = cx - p1[0]
    r1 = cy - p1[1]
    r = np.sqrt(r0 * r0 + r1 * r1)
    return (cx, cy, r)

def _make_circle_two_points(points, p, q):
    circ = make_diameter(p, q)
    left = None
    right = None
    pq = (q[1] - p[1], p[0] - q[0])
    for r in points:
        if is_in_circle(circ, r):
            continue
        cross = pq[0] * (r[1] - p[1]) - pq[1] * (r[0] - p[0])
        c = make_diameter(p, r)
        if cross > 0 and (left is None or pq[0] * (c[1] - left[1]) - pq[1] * (c[0] - left[0]) > 0):
            left = c
        elif cross < 0 and (right is None or pq[0] * (c[1] - right[1]) - pq[1] * (c[0] - right[0]) < 0):
            right = c

    if left is None and right is None:
        return circ
    if left is None:
        return right
    if right is None:
        return left
    if left[2] <= right[2]:
        return left
    return right


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



if __name__ == '__main__':
    points = [(0, 0), (1, 0), (0, 1), (1, 1)]
    circle = make_circle(points)
    print(circle)


