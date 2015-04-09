import threading


class TaskSubmitter:
    def __init__(self, robot):
        self.robot = robot
        self.thread = threading.Thread(target=self.robot.run)

    # Called when the robot needs to start running its state machine in a thread
    # or to start running a different state machine. Because each state handles
    # control for the next state, passing in a state will kick off a different state machine.
    def startNewTask(self, state):
        # If the robot's current state is not None, then we know that another state
        # is already running using the thread, so we need to shut down the
        # thread and wait until it is shutdown properly.
        if self.robot.currentState is not None:
            self.stop()         # Stop current thread
            self.thread.join()  # Wait until thread is finished

        self.robot.nextState(state)
        # Start the thread (again) with the new state. Note: This calls self.robot.run()
        self.thread.start()

    def stop(self):
        self.robot.stop()