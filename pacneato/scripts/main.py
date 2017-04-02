#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import Header
from nav_msgs.msg import Odometry
from cv_bridge import CvBridge
import cv2
import numpy as np
from coordinate_translator import coordinate_translator
from place_image import place_image
from tf.transformations import euler_from_quaternion

class Pacneato(object):
  def __init__(self):
    """ Initialize the video/game """
    rospy.init_node('pacneato')
    self.cv_image = None
    self.bridge = CvBridge()
    self.coins = [[2,1,0],[2,-1,0]]
    self.odom_pose = (0,0,0)
    self.focal = (626.813695,623.324624)     # Taken from calibration data
    self.principal = (326.583796,242.688526) # Taken from calibration data

    cv2.namedWindow('video_window')
    self.isub = rospy.Subscriber("/camera/image_raw", Image, self.process_img)
    self.osub = rospy.Subscriber('/odom', Odometry, self.process_odom)

  def process_img(self, msg):
    """ Process image messages from ROS and stash them in an attribute called
        cv_image for subsequent processing """
    self.cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding="bgra8")
    for c in coins:
      corners = [[c[0],c[1]+.1,c[2]+.1],
                 [c[0],c[1]-.1,c[2]+.1],
                 [c[0],c[1]-.1,c[2]-.1],
                 [c[0],c[1]+.1,c[2]-.1]]
      pts2 = [coordinate_translator(pt,
                                    self.odom_pose,
                                    self.focal,
                                    self.principal) for pt in corners]
      if False not in [((pt[0] <= 620) and 
                        (pt[0] >= 0) and
                        (pt[1] <= 480) and
                        (pt[1] >= 0)) for pt in pts2]:
        c_img_corners = []
        top = min([pt[1] for pt in pts2])
        bottom = max([pt[1] for pt in pts2])
        left = min([pt[0] for pt in pts2])
        right = max([pt[0] for pt in pts2])
        c_img = place_image(self.coin_img, pts2)
        for c in range(0,3):
          to_repl = (c_img[:,:,3]/255.0)
          repl = c_img[:,:,c] * to_repl
          orig = self.cv_image[top:bottom, left:right, c] * (1.0 - to_repl)
          self.cv_image[top:bottom, left:right, c] = repl + orig

  def process_odom(self, msg):
    """ Process odom messages from ROS and stash them in an attribute called
        odom_pose for subsequent processing """
    self.odom_pose = self.convert_pose_to_xy_and_theta(msg.pose.pose)

  def convert_pose_to_xy_and_theta(self, pose):
    """ A helper function to convert pose messages into something usable """
      orientation_tuple = (pose.orientation.x,
                           pose.orientation.y,
                           pose.orientation.z,
                           pose.orientation.w)
      angles = euler_from_quaternion(orientation_tuple)
      return (pose.position.x, pose.position.y, angles[2])

  def run(self):
    """ The main run loop """
    r = rospy.Rate(10)
    while not rospy.is_shutdown():
      if not self.cv_image is None:
        cv2.imshow('video_window', self.cv_image)
        cv2.waitKey(5)
      r.sleep()

if __name__ == '__main__':
  node = Pacneato()
  node.run()
