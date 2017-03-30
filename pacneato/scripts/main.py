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

        cv2.namedWindow('video_window')
        rospy.Subscriber("/camera/image_raw", Image, self.process_image)

    def process_image(self, msg):
        """ Process image messages from ROS and stash them in an attribute
            called cv_image for subsequent processing """
        pass

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
