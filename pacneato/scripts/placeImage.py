import cv2
import numpy as np
def placeImage (image,pts2):	
	"""Takes an image as input as well as the desired perspective of the image.
	Returns the transformed version of the image."""
	image = cv2.imread(img,-1)
	width = len(image[0])
	length = len(image)
	pts1 = [[0,0],[0,width],[length,width],[length,0]]
	M = cv2.getPerspectiveTransform(pts1,pts2)  #find homography instead?
	dst = cv2.warpPerspective(image,M,(length,width))
	return cropImage(dst)

def cropImage(image):
	for i in image:
		for x in i:
			if x[0] == 0 and x[1] == 0 and x[2] == 0:
				x[3] = 0
	return image


if __name__ == '__main__':
	image = "./test.png"
	cropImage(image)