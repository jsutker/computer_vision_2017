# Computer Vision: Pacneato
By Gabriel Butterick and Joseph Sutker

## Goal
The goal of our project was to allow a robot to visualize coins overlayed on its video feed in a way that accounted for changes in perspective. We wanted to then use that visualization to allow the driver of the robot to play a game collecting the various coins.

<video width="636" height="476" controls="controls">
  <source src="demo.mp4" type="video/mp4">
</video>

## Code
Our code is made up of the Pacneato object combined with a variety of class and helper functions that are used to overlay an image in a semi-realistic manner. We used a pinhole camera model to calculate where and how the overlayed image should appear on the video feed. Additionally, we accounted for distortion and perspective imposed by the camera lens by using a camera calibration function that used sampling to calculate the specific camera matrix as well as the distortion. Though that let us put the image in the correct place and make it fit with the rest of the feed, it did not address different perspectives. However, in order to warp the perspective of the image, we needed a transformation matrix. To get this, we used the OpenCV function getPerspectiveTransform, which takes two sets of points and determines what changes would need to be made to an image to make the view of the image make sense. We fed the resulting transformation matrix into the OpenCV warpPerspective function, which modifies an input image to reflect a viewpoint at a non-head on perspective.  Unfortunately, the warp perspective function applies a black background in places where it changes the image, which we wanted to avoid because it would ruin the illusion. We created a function that filters out all black pixels in the resulting image and makes them transparent. All these parts worked together to project a dynamic image at an appropriate, static position, that displayed correctly when viewed from any angle.

## Design Decision
At one point in the project, we were faced with the option of using either the OpenCV function findHomography or getPerspectiveTransform. Though findHomography is a more sophisticated version of getPerspectiveTransform, it also tends to make use of far more than the four points we had and is generally used when comparing images, not attempting to view them at another angle. In other words, it would be overkill. Meanwhile, getPerspectiveTransform only makes use of four points, as it is specifically designed for determining a transformation matrix of a single image based on four points from a given perspective. 

## Challenges
We had a bit of trouble actually getting the correct dimensions of the images we were working with. A major problem was that there was no image being overlayed initially, and we eventually found that we had essentially created impossible dimensions for the overlay image to be visible. This was an unfortunately difficult debugging process because it threw no errors and was part of a rather complex string of functions, any or all of which could have been the failure point. Ultimately, we found the problem by systematically combing the code and printing certain values to find the problem's origin.

## Future Work
We would like to have interesting lighting effects for the coins so they don't look so out of place. It would be neat if we could make the coins look so natural in their environment that people wondered if they were actually there instead of a computer projection. One way we would go about doing that is by having the coins disappear behind other objects, which we could use laserscan data to implement. We would also have made an effort to make the coins objects instead of instantiating them manually, and have a 'game start' function that randomly placed a number of coins around the robot.

## Big Takeaways
Through working on this project, researching necessary algorithms, and stumbling in a few places, we came upon a few useful insights for future assignments. Lenses and cameras as a whole greatly complicate what, on the surface, seems like a fairly easy task. The Pinhole Camera Model was an eye opening experience because of the way it forced us to change the way we thought about the video feed we were seeing. The possibility of using matrices to perform complex operations on large sets of data is likely to benefit us in future assignments. Though both of us are reticent to use them due to their relative complexity, they are quite useful for image alterations. 