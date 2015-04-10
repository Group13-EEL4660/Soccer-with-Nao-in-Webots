

# This class handles the case when a ball is in neither camera.
# It will look for the soccer ball by first rotating the head in the
# yaw left and right. If the ball is not found in any of the cameras
# rotate the body in the yaw. If the ball is not found, then have
# the robot walk in a random direction to keep searching.
class BallScanState:
    def __init__(self):
        pass

    def run(self, parent):

        pass