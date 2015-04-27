from StateEnums import StateEnums
import time


class DribbleBall:
    def __init__(self):
        self.__initDone = False
        self.__timeout = 8.0
        self.__endTime = None

    def run(self, parent):
        print "Dribble Ball"
        if self.__initDone is False:
            # Walk forward into the ball
            parent.motion.moveToward(1.0, 0.0, 0.0)
            # Start timer to timeout if ball does not appear in cameras in time
            self.__endTime = time.time() + self.__timeout
            self.__initDone = True
        else:
            topCameraBallLocation = parent.imageProcessor.objectLocationInCamera(0, "Ball")
            if topCameraBallLocation is not None:
                parent.nextState(StateEnums.FOLLOW_BALL)
            elif time.time() > self.__endTime:
                parent.nextState(StateEnums.WANDER_FOR_BALL)