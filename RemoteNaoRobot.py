

class RemoteNaoRobot:
    class NaoRobotBuilder:
        def __init__(self):
            self.motion = None
            self.robotPosture = None
            self.videoDevice = None

        def setMotion(self, motion):
            self.motion = motion
            return self

        def setRobotPosture(self, robotPosture):
            self.robotPosture = robotPosture
            return self

        def setVideoDevice(self, videoDevice):
            self.videoDevice = videoDevice
            return self

        def build(self):
            return RemoteNaoRobot(self.motion,
                                  self.robotPosture,
                                  self.videoDevice)

    def __init__(self, motion, robotPosture, videoDevice):
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