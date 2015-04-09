from states.soccer import BallScanState


class SoccerPrepState:
    def __init__(self):
        pass

    def run(self, parent):
        parent.motion.wakeUp()
        parent.posture.goToPosture("StandInit", 0.5)
        parent.nextState(BallScanState())
