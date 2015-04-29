from StateEnums import StateEnums


class AlignBallWithGoal:
    def __init__(self):
        self.__isRotationSet = False
        self.__alignedWithGoal = False
        self.__rotation = 0.19
        self.__goalKickPixelPercent = 0.37

    def run(self, parent):
        print "Aligning with ball"
        # When the goal is in the center of the screen, then stop rotating
        topCameraImage = parent.imageProcessor.getImageFromCamera(0)
        goalLocation = parent.imageProcessor.objectLocationInImage(topCameraImage, "Goal", True)
        if goalLocation is not None:
            print "Goal in sight. Location = " + str(goalLocation)
            # Align the goal in the center of the image
            anglesToGoal = parent.imageProcessor.videoDevice\
                .getAngularPositionFromImagePosition(0, [goalLocation[0], goalLocation[1]])
            if -0.03 < anglesToGoal[0] < 0.03:
                self.proceedToNextState(parent, topCameraImage)
            else:
                # Rotate towards goal
                self.rotateAroundBall(parent.motion, -anglesToGoal[0])
        elif self.__isRotationSet is False:
            print "Searching for goal"
            self.searchForGoal(parent.motion)

    def rotateAroundBall(self, motionProxy, robotYawAngle):
        if robotYawAngle < 0:
            # Rotate left, move right
            motionProxy.moveToward(0.0, -1.0, self.__rotation)
        else:
            # Rotate right, move left
            motionProxy.moveToward(0.0, 1.0, -self.__rotation)

    def searchForGoal(self, motionProxy):
        # Use absolute angle to determine whether to rotate around ball left or right
        robotAbsYawAngle = motionProxy.getRobotPosition(False)[2]
        print robotAbsYawAngle
        self.rotateAroundBall(motionProxy, robotAbsYawAngle)
        self.__isRotationSet = True

    def proceedToNextState(self, parent, image):
        # Stop all movement
        parent.motion.stopMove()
        # Goal approximately in the center
        # Get number of pixels that are above the threshold to judge the approximate
        # distance from the goal.
        pixelPercent = parent.imageProcessor.\
            objectDetector.percentageAboveThreshold(image, "Goal")
        if pixelPercent > self.__goalKickPixelPercent:
            parent.nextState(StateEnums.KICK_BALL)
        else:
            parent.nextState(StateEnums.DRIBBLE_BALL)
        # Need to reset to False just in case it is used as a singleton because it
        # must get a fresh rotation direction with each new aligning to the ball.
            self.__isRotationSet = False