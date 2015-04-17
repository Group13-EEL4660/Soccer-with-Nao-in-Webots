import vision_definitions


class FollowBall:
    def __init__(self):
        pass

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

        #if topCameraBallLoc is not None:
