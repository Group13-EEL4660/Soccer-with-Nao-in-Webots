

class TaskSubmitter:
    def __init__(self):
        self.currentTask = None

    # Called when start() is called from outside class.
    def run(self):
        self.currentTask.run()

    def nextTask(self, task):
        self.currentTask = task

    def stop(self):
        self.currentTask.stop()