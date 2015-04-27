from StateEnums import StateEnums


class AlignBallWithGoal:
    def __init__(self):
        self.__oriented = False
        self.__alignedWithGoal = False
        self.__rotation = 0.0

    def run(self, parent):
        print "Aligning with ball"
        # When the goal is in the center of the screen, then stop rotating
        topCameraImage = parent.imageProcessor.getImageFromCamera(0)
        goalLocation = parent.imageProcessor.objectLocationInImage(topCameraImage, "Goal", True)
        if goalLocation is not None:
            if self.__alignedWithGoal is False:
                # Align the goal in the center of the image
                anglesToGoal = parent.imageProcessor.videoDevice\
                    .getAngularPositionFromImagePosition(0, [goalLocation[0], goalLocation[1]])
                if -0.03 < anglesToGoal[0] < 0.03:
                    parent.motion.stopMove()
                    self.__alignedWithGoal = True
            else:
                # Goal approximately in the center
                # Get number of pixels that are above the threshold to judge the approximate
                # distance from the goal.
                pixelPercent = parent.imageProcessor.\
                    objectDetector.percentageAboveThreshold(topCameraImage, "Goal")
                print "pixel percent = " + str(pixelPercent)
                if pixelPercent > 0.35:  # More than 0.35% are yellow
                    parent.nextState(StateEnums.KICK_BALL)
                else:
                    parent.nextState(StateEnums.DRIBBLE_BALL)
                self.__oriented = False
        # Use absolute angle to determine whether to rotate around ball left or right
        if self.__oriented is False:
            robotAbsYawAngle = parent.motion.getRobotPosition(False)[2]
            if robotAbsYawAngle < 0:
                direction = -1.0  # Rotate left, move right
                self.__rotation = 0.19
            else:
                direction = 1.0  # Rotate right, move left
                self.__rotation = -0.19
            parent.motion.moveToward(0.0, direction, self.__rotation)
            self.__oriented = True
