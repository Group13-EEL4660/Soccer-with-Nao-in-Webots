from states.soccer.PrepareToPlay import PrepareToPlay
import vision_definitions
import time


class SoccerTask:
    def __init__(self,
                 imageProcessor,
                 motion,
                 robotPosture,
                 ballQueryImage,
                 startState=PrepareToPlay()):
        self.imageProcessor = imageProcessor
        self.motion = motion
        self.robotPosture = robotPosture
        self.ballQueryImage = ballQueryImage
        self.currentState = startState
        self.__stopped = False
        # Subscribe to needed camera feeds
        self.imageProcessor.subscribe(vision_definitions.kTopCamera)
        self.imageProcessor.subscribe(vision_definitions.kBottomCamera)

    def __del__(self):
        self.imageProcessor.unsubscribe(vision_definitions.kTopCamera)
        self.imageProcessor.unsubscribe(vision_definitions.kBottomCamera)

    def nextState(self, state):
        self.currentState = state

    def run(self):
        while self.__stopped is False:
            priorTime = time.time()
            self.currentState.run(self)
            # Allows for a steady rate for self.currentState.run() to be called at.
            time.sleep((1.0 / self.imageProcessor.cameraFPS) - (time.time() - priorTime))

    def stop(self):
        print("Stopped made True")
        self.__stopped = True