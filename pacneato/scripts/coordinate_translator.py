def coordinate_translator(world_coords, odom_coords, focal_point, principal_point):
  w_x, w_y, w_z = world_coords
  o_x, o_y, o_theta = odom_coords
  fx, fy = focal_point
  cx, cy = principal_point

  t = (_,_,_)
  rx = (_,_,_)
  ry = (_,_,_)
  rz = (_,_,_)

  x = t[0] + (w_x*rx[0]) + (w_y*rx[1]) + (w_z*rx[2])
  y = t[1] + (w_x*ry[0]) + (w_y*ry[1]) + (w_z*ry[2])
  z = t[2] + (w_x*rz[0]) + (w_y*rz[1]) + (w_z*rz[2])

  u = (fx*(x/z))+cx
  v = (fy*(y/z))+cy

  return (u, v)