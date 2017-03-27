import cv2
import numpy as np
def placeImage (image,pts2):	
	"""Takes an image as input as well as the desired perspective of the image.
	Returns the transformed version of the image."""
	
	width = len(image[0])
	length = len(image)
	pts1 = [[0,0],[0,width],[length,width],[length,0]]
	M = cv2.getPerspectiveTransform(pts1,pts2)  #find homography instead?
    dst = cv2.warpPerspective(image,M,(length,width))
    return dst
