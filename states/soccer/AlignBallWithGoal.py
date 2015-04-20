import numpy as np
import math
from StateEnums import StateEnums


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
        distanceToGoal = math.sqrt(math.pow(vectorToGoal[0], 2) +
                                   math.pow(vectorToGoal[1], 2))
        unitVectorToGoal = np.divide(vectorToGoal, distanceToGoal)
        direction = math.atan(unitVectorToGoal[1] / unitVectorToGoal[0])
        normDirection = direction / math.pi
        headYawAngle = parent.motion.getAngles("HeadYaw", True)
        print normDirection, headYawAngle
        error = 0.1
        deltaAngle = normDirection - headYawAngle[0]
        if deltaAngle > error:
            parent.motion.moveToward(0.0, 1.0, -0.2, [["Frequency", 1.0]])  # Move right, rotate left
        elif deltaAngle < -error:
            parent.motion.moveToward(0.0, -1.0, 0.2, [["Frequency", 1.0]])  # Move left, rotate right
        else:
            # Aligned with ball. Check distance from goal to see if robot
            # should attempt to kick ball into the goal. If not in radius, then
            # just walk into the ball to move it closer.
            if distanceToGoal < 10.0:
                # Kick
                parent.nextState(StateEnums.KICK_BALL)
            else:
                parent.motion.moveToward(1.0, 0.0, 0.0, [["Frequency", 1.0]])
