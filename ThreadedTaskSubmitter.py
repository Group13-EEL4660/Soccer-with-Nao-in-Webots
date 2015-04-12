import threading


class ThreadedTaskSubmitter:
    def __init__(self, taskSubmitter):
        self.__taskSubmitter = taskSubmitter
        self.__thread = None

    # Called when the robot needs to start running a new task. The first state to
    # execute in the new task is the state passed as a parameter.
    def startNewTask(self, task):
        if self.__thread is not None:
            print("Thread exists, stopping it.")
            self.stopTask()         # Stop current thread and wait for it to close
        # Must create a new thread, because a thread can only be started once.
        # Passing in the robot's run function so that when the threads start function
        # is called, it will call self.robot.run()
        self.__thread = threading.Thread(target=self.__taskSubmitter.run)
        self.__taskSubmitter.nextTask(task)
        self.__thread.start()

    def stopTask(self):
        self.__taskSubmitter.stop()   # Cleanly stop the robot's run loop
        self.waitTask()

    def waitTask(self):
        self.__thread.join()  # Wait until the thread is finished