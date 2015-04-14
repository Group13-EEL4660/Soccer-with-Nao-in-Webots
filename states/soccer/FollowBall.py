import vision_definitions


class FollowBall:
    def __init__(self):
        pass

    def run(self, parent):
        print("Follow Ball")
        # Check if the ball is in the top camera
        topCameraBallLoc = parent.imageProcessor.objectLocationInCamera(
            vision_definitions.kTopCamera,
            parent.ballQueryImage,
            threshold
        )
        pass