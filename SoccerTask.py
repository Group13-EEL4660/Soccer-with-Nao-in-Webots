from StateEnums import StateEnums
from states.soccer.PrepareToPlay import PrepareToPlay
from states.soccer.WanderForBall import WanderForBall
from states.soccer.FollowBall import FollowBall
from states.soccer.AlignBallWithGoal import AlignBallWithGoal
from states.soccer.KickBall import KickBall
import vision_definitions
import time


class SoccerTask:
    def __init__(self,
                 imageProcessor,
                 motion,
                 robotPosture,
                 goalPosition,
                 startState=PrepareToPlay()):
        self.imageProcessor = imageProcessor
        self.motion = motion
        self.robotPosture = robotPosture
        self.goalPosition = goalPosition
        self.currentState = startState
        self.__stopped = False
        # Subscribe to needed camera feeds
        self.imageProcessor.subscribe(vision_definitions.kTopCamera)
        self.imageProcessor.subscribe(vision_definitions.kBottomCamera)

    def __del__(self):
        self.imageProcessor.unsubscribe(vision_definitions.kTopCamera)
        self.imageProcessor.unsubscribe(vision_definitions.kBottomCamera)

    def nextState(self, state):
        if state == StateEnums.PREPARE_TO_PLAY:
            self.currentState = PrepareToPlay()
        elif state == StateEnums.WANDER_FOR_BALL:
            self.currentState = WanderForBall()
        elif state == StateEnums.FOLLOW_BALL:
            self.currentState = FollowBall()
        elif state == StateEnums.ALIGN_BALL_WITH_GOAL:
            self.currentState = AlignBallWithGoal()
        elif state == StateEnums.KICK_BALL:
            self.currentState = KickBall()

    def run(self):
        self.__stopped = False
        while self.__stopped is False:
            priorTime = time.time()
            self.currentState.run(self)
            #self.nextState(nextState)
            # Allows for a steady rate for self.currentState.run() to be called at.
            sleepTime = (1.0 / self.imageProcessor.cameraFPS) - (time.time() - priorTime)
            if sleepTime > 0.0:
                time.sleep(sleepTime)

    def stop(self):
        print("Stopped made True")
        self.__stopped = True