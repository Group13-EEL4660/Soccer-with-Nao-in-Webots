from states.soccer.WanderForBall import WanderForBall


class PrepareToPlay:
    def __init__(self):
        self.__hasStarted = False
        self.__wakeUpID = 0
        self.__postureID = 0

    def run(self, parent):
        print("PrepareToPlay")
        if self.__hasStarted is False:
            self.__wakeUpID = parent.motion.post.wakeUp()
            self.__postureID = parent.robotPosture.post.goToPosture("StandInit", 0.5)
            self.__hasStarted = True

        if parent.motion.isRunning(self.__wakeUpID) is False and\
            parent.robotPosture.isRunning(self.__postureID) is False:
            # The call to goToPosture has finished, so the state can now be changed
            parent.nextState(WanderForBall())
