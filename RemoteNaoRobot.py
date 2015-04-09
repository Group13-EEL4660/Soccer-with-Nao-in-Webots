from naoqi import ALProxy
import threading


class RemoteNaoRobot:
    def __init__(self, ip, port):
        self.motion = ALProxy("ALMotion", ip, port)
        self.posture = ALProxy("ALRobotPosture", ip, port)
        self.video = ALProxy("ALVideoDevice", ip, port)
        self.currentState = None
        self.isRunning = True

    # Called when start() is called from outside class.
    def run(self):
        while self.isRunning is True:
            self.currentState.run(self)

    def nextState(self, state):
        self.currentState = state

    def stop(self):
        self.isRunning = False