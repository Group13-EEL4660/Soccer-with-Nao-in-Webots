from StateEnums import StateEnums
from states.soccer.PrepareToPlay import PrepareToPlay
from states.soccer.WanderForBall import WanderForBall
from states.soccer.FollowBall import FollowBall
from states.soccer.ApproachBall import ApproachBall
from states.soccer.AlignBallWithGoal import AlignBallWithGoal
from states.soccer.KickBall import KickBall
from states.soccer.DribbleBall import DribbleBall
from states.soccer.AvoidObstacle import AvoidObstacle
from states.soccer.DefendGoal import DefendGoal
import time


class SoccerTask:
    def __init__(self,
                 imageProcessor,
                 motion,
                 robotPosture,
                 position,
                 startState):
        self.imageProcessor = imageProcessor
        self.motion = motion
        self.robotPosture = robotPosture
        self.currentState = startState
        self.position = position
        self.__stopped = False
        # Subscribe to needed camera feeds
        self.imageProcessor.subscribe(0)
        self.imageProcessor.subscribe(1)

    def __del__(self):
        self.imageProcessor.unsubscribe(0)
        self.imageProcessor.unsubscribe(1)

    def nextState(self, state):
        if state == StateEnums.PREPARE_TO_PLAY:
            self.currentState = PrepareToPlay()
        elif state == StateEnums.WANDER_FOR_BALL:
            self.currentState = WanderForBall()
        elif state == StateEnums.FOLLOW_BALL:
            self.currentState = FollowBall()
        elif state == StateEnums.APPROACH_BALL:
            self.currentState = ApproachBall()
        elif state == StateEnums.ALIGN_BALL_WITH_GOAL:
            self.currentState = AlignBallWithGoal()
        elif state == StateEnums.KICK_BALL:
            self.currentState = KickBall()
        elif state == StateEnums.DRIBBLE_BALL:
            self.currentState = DribbleBall()
        elif state == StateEnums.AVOID_OBSTACLE:
            self.currentState = AvoidObstacle()
        elif state == StateEnums.DEFEND_GOAL:
            self.currentState = DefendGoal()

    def run(self):
        self.__stopped = False
        while self.__stopped is False:
            priorTime = time.time()
            self.currentState.run(self)
            # Allows for a steady rate for self.currentState.run() to be called at.
            sleepTime = (1.0 / self.imageProcessor.cameraFPS) - (time.time() - priorTime)
            if sleepTime > 0.0:
                time.sleep(sleepTime)

    def stop(self):
        print("Stopped made True")
        self.__stopped = True