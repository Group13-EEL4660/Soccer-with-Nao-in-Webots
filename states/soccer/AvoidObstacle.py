import time
from StateEnums import StateEnums


class AvoidObstacle:
    def __init__(self):
        pass

    def run(self, parent):
        print "Avoid Obstacle"
        obstacleLocation = parent.imageProcessor.objectLocationInCamera(0, "Obstacle")
        if obstacleLocation is None:
                parent.nextState(StateEnums.FOLLOW_BALL)
        else:
            self.reactToObstacle(parent.motion, obstacleLocation[0])

    def reactToObstacle(self, motionProxy, normObstacleLocationX):
        # Determine whether the obstacle is on the left or right side
        if normObstacleLocationX > 0.5:
            # Shift left
            motionProxy.moveToward(0.0, 1.0, 0.0)
        else:
            # Shift right
            motionProxy.moveToward(0.0, -1.0, 0.0)