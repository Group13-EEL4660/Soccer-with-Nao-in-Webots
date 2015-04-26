import vision_definitions
from StateEnums import StateEnums
import math


class FollowBall:
    def __init__(self):
        self.headID = None

    def run(self, parent):
        print("Follow Ball")
        topImage = parent.imageProcessor.getImageFromCamera(0)#vision_definitions.kTopCamera)

        # Check for an obstacle in the top camera (i.e. another robot in the way).
        # If none, then continue to the ball. If there is an obstacle determine whether
        # it is on the right or left and move opposite to it

        topCameraBallLoc = parent.imageProcessor.objectLocationInImage(topImage, "Ball", True)
        # Check if the ball is in the top camera
        # topCameraBallLoc = parent.imageProcessor.objectLocationInCamera(
        #     vision_definitions.kTopCamera,
        #     "Ball"
        # )

        if topCameraBallLoc is not None:
            headAnglesToBall = parent.imageProcessor.videoDevice\
                .getAngularPositionFromImagePosition(0,#vision_definitions.kTopCamera,
                                                     [topCameraBallLoc[0], topCameraBallLoc[1]])
            if self.headID is not None:
                parent.motion.stop(self.headID)
            self.headID = parent.motion.post.angleInterpolation(
                ["HeadYaw", "HeadPitch"],
                [headAnglesToBall[0], headAnglesToBall[1]],
                0.6,
                False
            )
            # Gets the yaw angle of the head according to the sensor angles
            headYawAngle = parent.motion.getAngles("HeadYaw", False)
            # Apply a velocity in the direction the head is turned
            parent.motion.moveToward(1.0, 0.0, headYawAngle[0]/math.pi, [["Frequency", 1.0]])
        else:
            bottomCameraBallLoc = parent.imageProcessor.objectLocationInCamera(
                1,#vision_definitions.kBottomCamera,
                "Ball"
            )
            if bottomCameraBallLoc is not None:
                parent.motion.stopMove()    # Stop moving
                parent.nextState(StateEnums.ALIGN_BALL_WITH_GOAL)
            else:
                parent.motion.stopMove()    # Stop moving
                parent.nextState(StateEnums.WANDER_FOR_BALL)