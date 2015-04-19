import vision_definitions
from StateEnums import StateEnums


class FollowBall:
    def __init__(self):
        self.headID = None

    def run(self, parent):
        print("Follow Ball")
        # Step 1 - Get yaw and pitch angles between head and ball
        # Step 2 - Set the head's angles accordingly
        # Step 3 - Get the yaw angle between the body and the head
        # Apply that angle to the moveToward function

        # Check if the ball is in the top camera
        topCameraBallLoc = parent.imageProcessor.objectLocationInCamera(
            vision_definitions.kTopCamera,
            parent.imageProcessor.objectDetector.queryThresholdDict["Ball"][0],
            parent.imageProcessor.objectDetector.queryThresholdDict["Ball"][1]
        )

        if topCameraBallLoc is not None:
            headAnglesToBall = parent.imageProcessor.videoDevice\
                .getAngularPositionFromImagePosition(vision_definitions.kTopCamera,
                                                     [topCameraBallLoc[0], topCameraBallLoc[1]])
            if self.headID is not None:
                parent.motion.stop(self.headID)
            self.headID = parent.motion.post.changeAngles(
                    ["HeadYaw", "HeadPitch"], [headAnglesToBall[0], headAnglesToBall[1]], 0.1
            )
        else:
            bottomCameraBallLoc = parent.imageProcessor.objectLocationInCamera(
                vision_definitions.kBottomCamera,
                parent.imageProcessor.objectDetector.queryThresholdDict["Ball"][0],
                parent.imageProcessor.objectDetector.queryThresholdDict["Ball"][1]
            )
            if bottomCameraBallLoc is not None:
                parent.nextState(StateEnums.ALIGN_BALL_WITH_GOAL)
            else:
                parent.nextState(StateEnums.FOLLOW_BALL)