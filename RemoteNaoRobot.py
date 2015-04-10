

class RemoteNaoRobot:
    def __init__(self, motion=None, robotPosture=None, videoDevice=None):
        self.motion = motion
        self.robotPosture = robotPosture
        self.videoDevice = videoDevice
        self.currentState = None
        self.stopped = False

    # Called when start() is called from outside class.
    def run(self):
        self.stopped = False
        while self.stopped is False:
            self.currentState.run(self)

    def nextState(self, state):
        self.currentState = state

    def stop(self):
        self.stopped = True