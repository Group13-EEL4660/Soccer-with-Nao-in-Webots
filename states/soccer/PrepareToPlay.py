from StateEnums import StateEnums
from SoccerPositions import SoccerPositions


class PrepareToPlay:
    def __init__(self):
        self.__hasStarted = False
        self.__wakeUpID = 0
        self.__postureID = 0
        self.count = 0

    def run(self, parent):
        #print self.count
        self.count += 1
        if self.__hasStarted is False:
            self.__wakeUpID = parent.motion.post.wakeUp()
            self.__postureID = parent.robotPosture.post.goToPosture("StandInit", 0.5)
            self.__hasStarted = True

        if parent.motion.isRunning(self.__wakeUpID) is False and\
            parent.robotPosture.isRunning(self.__postureID) is False:
            if parent.position is SoccerPositions.OFFENSE:
                # The call to goToPosture has finished, so the state can now be changed
                parent.nextState(StateEnums.WANDER_FOR_BALL)
            else:
                parent.nextState(StateEnums.DEFEND_GOAL)