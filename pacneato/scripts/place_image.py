import cv2
import numpy as np
def place_image(img,pts2):	
	"""Takes an image as input as well as the desired perspective of the image.
	Returns the transformed version of the image."""
	image = cv2.imread(img,-1)
	width = len(image[0])-1
	length = len(image)-1
	pts1 = np.array([[0,0],[0,width],[length,width],[length,0]],np.float32)
	top = int(round(min([pt[1] for pt in pts2])))
	bottom = int(round(max([pt[1] for pt in pts2])))
	left = int(round(min([pt[0] for pt in pts2])))
	right = int(round(max([pt[0] for pt in pts2])))
	pts2 = np.array([[pt[0]-left,pt[1]-top] for pt in pts2],np.float32)
	M = cv2.getPerspectiveTransform(pts1,pts2)  #find homography instead?
	dst = cv2.warpPerspective(image,M,(right-left,bottom-top))
	return crop_image(dst)

def crop_image(image):
	for i in image:
		for x in i:
			if x[0] == 0 and x[1] == 0 and x[2] == 0:
				x[3] = 0
	return image


if __name__ == '__main__':
	image = "coin.png"
	crop_image(cv2.imread(image,-1))