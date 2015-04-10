from states.soccer.BallScanState import BallScanState


class SoccerPrepState:
    def __init__(self):
        pass

    def run(self, parent):
        parent.motion.wakeUp()
        parent.robotPosture.goToPosture("StandInit", 0.5)
        parent.nextState(BallScanState())
