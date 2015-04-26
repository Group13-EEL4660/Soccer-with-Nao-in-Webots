import numpy as np
import math
from StateEnums import StateEnums
import vision_definitions


class AlignBallWithGoal:
    def __init__(self):
        pass

    def run(self, parent):
        print("Align Ball with Goal")
        # Look up for goal. Use top camera to find goal and bottom camera to know ball is in view
        parent.motion.setAngles("HeadPitch", 0.0, 1.0)
        #ballLocation = parent.imageProcessor.objectLocationInCamera(0, "Ball")
        #robotAbsYawAngle = parent.motion.getRobotPosition(False)[2]
