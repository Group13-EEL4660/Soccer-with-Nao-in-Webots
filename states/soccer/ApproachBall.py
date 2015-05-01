from StateEnums import StateEnums


class ApproachBall:
    def __init__(self):
        pass

    def run(self, parent):
        #print("Approach Ball")
        topCameraObstacleLoc = parent.imageProcessor.objectLocationInCamera(0, "Obstacle")
        if topCameraObstacleLoc is not None:
            # Avoid the obstacle
            parent.nextState(StateEnums.AVOID_OBSTACLE)
        # Check if the ball is in the bottom camera
        bottomCameraBallLoc = parent.imageProcessor.objectLocationInCamera(1, "Ball")
        if bottomCameraBallLoc is not None:
            if bottomCameraBallLoc[1] > 0.95:
                parent.motion.stopMove()
                parent.nextState(StateEnums.ALIGN_BALL_WITH_GOAL)
            anglesToBall = parent.imageProcessor.videoDevice\
                .getAngularPositionFromImagePosition(1, [bottomCameraBallLoc[0], bottomCameraBallLoc[1]])

            # Apply a velocity in the direction the head is turned
            parent.motion.moveToward(1.0, 0.0, anglesToBall[0], [["Frequency", 1.0]])

        else:
            topCameraBallLoc = parent.imageProcessor.objectLocationInCamera(0, "Ball")
            if topCameraBallLoc is not None:
                parent.nextState(StateEnums.FOLLOW_BALL)
            else:
                parent.motion.stopMove()    # Stop moving
                parent.nextState(StateEnums.WANDER_FOR_BALL)