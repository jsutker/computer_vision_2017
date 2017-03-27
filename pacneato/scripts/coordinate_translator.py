import numpy as np
from tf.transformations import rotation_matrix
def coordinate_translator(world_coords, odom_coords, focal_point, principal_point):
  w_z, w_x, w_y = world_coords
  o_x, o_y, o_theta = odom_coords
  fx, fy = focal_point
  cx, cy = principal_point

  t = (w_x-o_x, w_y-o_y, w_z)

  r = rotation_matrix(o_theta, (0,0,1))

  rx = r[0][:3]
  ry = r[1][:3]
  rz = r[2][:3]

  x = t[0] + (w_x*rx[0]) + (w_y*rx[1]) + (w_z*rx[2])
  y = t[1] + (w_x*ry[0]) + (w_y*ry[1]) + (w_z*ry[2])
  z = t[2] + (w_x*rz[0]) + (w_y*rz[1]) + (w_z*rz[2])

  u = (fx*(x/z))+cx
  v = (fy*(y/z))+cy

  return (u, v)