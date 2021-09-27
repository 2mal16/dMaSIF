import numpy as np

#files must be converted to npy (for faster read time)

from plyfile import PlyData
import numpy as np
import torch
from geometry_processing import save_vtk

filename = "./mesh_playground/1A0G_A.ply"
output_filename = "./mesh_playground/1A0G_A_custom.vtk"

# The ply files have all the information. We need the surface.

plydata = PlyData.read(filename)
triangles = np.vstack(plydata["face"].data["vertex_indices"])

points = np.vstack([[v[0], v[1], v[2]] for v in plydata["vertex"]])
points = points - np.mean(points, axis=0, keepdims=True)

values = np.zeros(shape = (points.shape[0],3))

for vertice_index in range(1000):
    values[vertice_index,:] = np.array([255,0,0])

# torchify them
points = torch.tensor(points, dtype = torch.float32)
triangles = torch.tensor(triangles, dtype = torch.int64)
values = torch.tensor(values, dtype = torch.float32)

# import pdb; pdb.set_trace()

save_vtk(output_filename,
        xyz = points,
        triangles = triangles,
        values = values)