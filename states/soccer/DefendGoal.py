class DefendGoal:
    def __init__(self):
        self.maxLateralDistance = 1.5
        self.lastBallLocation = (0.0, 0.0)
        self.haltDelta = 0.0

    def run(self, parent):
        #print "Defend Goal"
        ballLocation = parent.imageProcessor.objectLocationInCamera(0, "Ball")
        if ballLocation is not None:
            self.lastBallLocation = ballLocation
            ballLocation = parent.imageProcessor.objectLocationInCamera(1, "Ball")
            if ballLocation is not None:
                self.lastBallLocation = ballLocation
        self.moveGoalie(parent.motion)

    def moveGoalie(self, motionProxy):
        print motionProxy.getRobotPosition(False)
        if self.lastBallLocation[0] > 0.5 + self.haltDelta:
            print "Last ball location > 0.5"
            if motionProxy.getRobotPosition(False)[1] < -self.maxLateralDistance:
                motionProxy.stopMove()
            else:
                motionProxy.moveToward(0.0, -1.0, 0.0)
        elif self.lastBallLocation[0] < 0.5 - self.haltDelta:
            print "Last ball location <= 0.5"
            if motionProxy.getRobotPosition(False)[1] > self.maxLateralDistance:
                motionProxy.stopMove()
            else:
                motionProxy.moveToward(0.0, 1.0, 0.0)
        else:
            motionProxy.stopMove()