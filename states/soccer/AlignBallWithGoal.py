import numpy as np
import math

class AlignBallWithGoal:
    def __init__(self):
        pass

    def run(self, parent):
        print("Align Ball with Goal")
        # Rotate around the ball until the ball is in between the robot
        # and the goal. This is done by getting the unit vector from the
        # robot to the goal. Then getting the direction of the unit vector
        # and stopping the robots rotation around the ball when its direction
        # matches the direction of the vector within a certain delta.
        robotPosition = parent.motion.getRobotPosition(True)
        robotPos2D = (robotPosition[0], robotPosition[2])
        vectorToGoal = np.subtract(parent.goalPosition, robotPos2D)
        unitVectorToGoal = np.divide(vectorToGoal,
                                     math.sqrt(math.pow(vectorToGoal[0], 2) +
                                               math.pow(vectorToGoal[1], 2)))
        direction = math.atan(unitVectorToGoal[1] / unitVectorToGoal[0])
        normDirection = direction / math.pi
        print normDirection