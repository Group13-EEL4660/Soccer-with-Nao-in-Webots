from naoqi import ALProxy
import threading2 as threading


class RemoteNaoRobot:
    def __init__(self, ip, port):
        self.motion = ALProxy("ALMotion", ip, port)
        self.posture = ALProxy("ALRobotPosture", ip, port)
        self.video = ALProxy("ALVideoDevice", ip, port)
        self.currentState = None
        self.event = threading.Event()
        self.thread = threading.Thread(None, self)

    # Called when the robot needs to start running its state machine in a thread
    # or to start running a different state machine. Because each state handles
    # control for the next state, passing in a state will kick off a different state machine.
    def startNewTask(self, state):
        # If the current state is not None, then we know that another state
        # is already running using the thread, so we need to shut down the
        # thread and wait until it is shutdown properly.
        if self.currentState is not None:
            self.stop()         # Stop current thread
            self.thread.join()  # Wait until thread is finished

        self.currentState = state
        # Start the thread (again) with the new state. Note: This calls self.run()
        self.thread.start()

    def stop(self):
        self.event.set()

    # Called when start() is called from outside class.
    def run(self):
        while self.event.isSet() is not True:
            self.currentState.run(self)

    def nextState(self, state):
        self.currentState = state

