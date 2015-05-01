class DefendGoal:
    def __init__(self):
        pass

    def run(self, parent):
        print "Defend Goal"
        parent.motion.moveToward(1.0, 0.0, 0.0)
        pass