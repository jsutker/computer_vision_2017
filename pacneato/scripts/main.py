#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
from coordinate_translator import coordinate_translator
from placeImage import placeImage

class Pacneato(object):
  def __init__(self):
    """ Initialize the video/game """
    rospy.init_node('pacneato')
    self.cv_image = None
    self.coins = [[2,1,0],[2,-1,0]]

    cv2.namedWindow('video_window')
    rospy.Subscriber("/camera/image_raw", Image, self.process_image)
    self.sub = rospy.Subscriber('/odom', Odometry, self.process_odom)

  def process_image(self, msg):
    """ Process image messages from ROS and stash them in an attribute
        called cv_image for subsequent processing """
    coin_imgs = []
    for c in coins:
      corners = [[c[0],c[1]+.1,c[2]+.1],
                 [c[0],c[1]-.1,c[2]+.1],
                 [c[0],c[1]-.1,c[2]-.1],
                 [c[0],c[1]+.1,c[2]-.1]]
      pts2 = [coordinate_translator(pt) for pt in corners]
      c_img = placeImage(self.coin_img, pts2)
      coin_imgs.append([c_img,corners])
    ### DO OVERLAYING CODE HERE AND SAVE TO self.cv_image!!!!!

  def run(self):
    """ The main run loop"""
    r = rospy.Rate(10)
    while not rospy.is_shutdown():
      if not self.cv_image is None:
        cv2.imshow('video_window', self.cv_image)
        cv2.waitKey(5)
      r.sleep()

if __name__ == '__main__':
  node = Pacneato()
  node.run()
