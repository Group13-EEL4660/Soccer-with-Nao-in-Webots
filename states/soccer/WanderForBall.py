import vision_definitions
from FollowBall import FollowBall
from AlignBallWithGoal import AlignBallWithGoal


class WanderForBall:
    def __init__(self):
        self.__isExecuting = False
        self.__headMovementID = None

    def run(self, parent):
        print("WanderForBall")
        # Check if the ball is in the top camera
        topCameraBallLoc = parent.imageProcessor.objectLocationInCamera(
            vision_definitions.kTopCamera,
            parent.imageProcessor.objectDetector.queryThresholdDict["Ball"][0],
            parent.imageProcessor.objectDetector.queryThresholdDict["Ball"][1]
        )

        if topCameraBallLoc is None:
            # Check if the ball is in the bottom camera's view
            bottomCameraBallLoc = parent.imageProcessor.objectLocationInCamera(
                vision_definitions.kBottomCamera,
                parent.imageProcessor.objectDetector.queryThresholdDict["Ball"][0],
                parent.imageProcessor.objectDetector.queryThresholdDict["Ball"][1]
            )
            if bottomCameraBallLoc is None:
                if self.__isExecuting is False:
                    print("isExecuting is false")
                    # Interpolate head left then right.
                    names = ["HeadYaw"]
                    angleLists = [-2.0, 2.0, 0.0]  # Turn right to -2 radians then left to 2 radians
                    timeLists = [5.0, 10.0, 15.0]
                    self.__headMovementID = parent.motion.post.angleInterpolation(
                        names,
                        angleLists,
                        timeLists,
                        True
                    )
                    self.__isExecuting = True
                else:
                    print("isExecuting is true")
                    # Check if the robot's head movement thread is complete.
                    if parent.motion.isRunning(self.__headMovementID) is False:
                        print("motion thread has stopped running")
                        # Angle interpolation is complete.
                        self.__isExecuting = False
            else:
                # Ball is in the bottom camera's view, so go to BottomCameraState
                if self.__headMovementID is not None:
                    parent.motion.stop(self.__headMovementID)
                parent.nextState(AlignBallWithGoal())
        else:
            if self.__headMovementID is not None:
                parent.motion.stop(self.__headMovementID)
            parent.nextState(FollowBall())