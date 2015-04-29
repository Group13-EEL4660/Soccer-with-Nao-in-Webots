from StateEnums import StateEnums
import cv2


class WanderForBall:
    def __init__(self):
        pass

    def run(self, parent):
        print("WanderForBall")
        # Check if the ball is in the top camera
        topCameraBallLoc = parent.imageProcessor.objectLocationInCamera(0, "Ball")
        if topCameraBallLoc is None:
            # Check if the ball is in the bottom camera's view
            bottomCameraBallLoc = parent.imageProcessor.objectLocationInCamera(1, "Ball")
            if bottomCameraBallLoc is None:
                parent.motion.moveToward(0.0, 0.0, -1.0)
            else:
                parent.motion.stopMove()
                parent.nextState(StateEnums.APPROACH_BALL)
        else:
            parent.motion.stopMove()
            parent.nextState(StateEnums.FOLLOW_BALL)