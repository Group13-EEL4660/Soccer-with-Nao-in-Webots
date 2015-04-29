from StateEnums import StateEnums


class FollowBall:
    def __init__(self):
        pass

    def run(self, parent):
        print("Follow Ball")
        topCameraObstacleLoc = parent.imageProcessor.objectLocationInCamera(0, "Obstacle")
        if topCameraObstacleLoc is not None:
            # Avoid the obstacle
            parent.nextState(StateEnums.AVOID_OBSTACLE)
        # Check if the ball is in the top camera
        topCameraBallLoc = parent.imageProcessor.objectLocationInCamera(0, "Ball")
        if topCameraBallLoc is not None:
            anglesToBall = parent.imageProcessor.videoDevice\
                .getAngularPositionFromImagePosition(0, [topCameraBallLoc[0], topCameraBallLoc[1]])

            # Apply a velocity in the direction the head is turned
            parent.motion.moveToward(1.0, 0.0, anglesToBall[0], [["Frequency", 1.0]])
        else:
            bottomCameraBallLoc = parent.imageProcessor.objectLocationInCamera(1, "Ball")
            if bottomCameraBallLoc is not None:
                parent.nextState(StateEnums.APPROACH_BALL)
            else:
                parent.motion.stopMove()    # Stop moving
                parent.nextState(StateEnums.WANDER_FOR_BALL)