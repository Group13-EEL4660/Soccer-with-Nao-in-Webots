from StateEnums import StateEnums
import almath
import motion as mot
import sys


class KickBall:
    def __init__(self):
        self.__xDiffThreshold = 0.139
        self.__yDiffThreshold = 0.208
        self.__postureID = None
        self.__initDone = False
        self.__footNormPixelLoc = (0.25, 0.7)

    def run(self, parent):
        print "Kick Ball"
        parent.motion.setAngles("HeadPitch", 0.5, 1.0)
        ballLocation = parent.imageProcessor.objectLocationInCamera(1, "Ball")
        if self.__initDone is False and ballLocation is not None:
            diffX = self.__footNormPixelLoc[0] - ballLocation[0]
            diffY = self.__footNormPixelLoc[1] - ballLocation[1]

            # Line up with ball horizontally first, then vertically. Once both are lined up, then kick.
            if abs(diffX) >= self.__xDiffThreshold:
                # Move horizontally
                relativeVelY = diffX / abs(diffX)
                parent.motion.moveToward(0.0, relativeVelY, 0.0)
            elif abs(diffY) >= self.__yDiffThreshold:
                # Move slowly vertically
                relativeVelX = (diffY / abs(diffY)) * 0.6
                parent.motion.moveToward(relativeVelX, 0.0, 0.0)
            else:
                parent.motion.stopMove()
                self.__postureID = parent.robotPosture.post.goToPosture("StandInit", 0.5)
                self.__initDone = True
        elif self.__initDone and parent.robotPosture.isRunning(self.__postureID) is False:
            # It is finished getting into standing posture, so now kick the ball
            self.kick(parent.motion)
            parent.robotPosture.goToPosture("StandInit", 0.5)
            parent.nextState(StateEnums.WANDER_FOR_BALL)

    def shift_weight(self, use_sensor_values, motion_proxy):
        axis_mask = almath.AXIS_MASK_ALL   # full control

        # Lower the Torso and move to the side
        effector = "Torso"
        frame = mot.FRAME_ROBOT
        times = 2.0  # seconds
        try:
            init_tf = almath.Transform(motion_proxy.getTransform(effector, frame, use_sensor_values))
        except Exception as e:
            sys.exit(e)
        delta_tf = almath.Transform(0.0, -0.06, -0.03)  # x, y, z
        target_tf = init_tf * delta_tf
        path = list(target_tf.toVector())
        motion_proxy.transformInterpolation(effector, frame, path, axis_mask, times, True)

        # Lift LLeg
        effector = "LLeg"
        frame = mot.FRAME_TORSO
        times = 2.0  # seconds
        try:
            init_tf = almath.Transform(motion_proxy.getTransform(effector, frame, use_sensor_values))
        except Exception as e:
            sys.exit(e)
        delta_tf = almath.Transform(0.0, 0.0, 0.04)
        target_tf = init_tf * delta_tf
        path = list(target_tf.toVector())
        motion_proxy.transformInterpolation(effector, frame, path, axis_mask, times, True)

    def kick(self, motion_proxy):
        frame = mot.FRAME_TORSO
        axis_mask = almath.AXIS_MASK_ALL   # full control
        use_sensor_values = False

        self.shift_weight(use_sensor_values, motion_proxy)
        # move LLeg back
        effector = "LLeg"
        times = 4.0     # seconds
        current_pos = motion_proxy.getPosition(effector, frame, use_sensor_values)
        target_pos = almath.Position6D(current_pos)
        target_pos.x -= 0.1
        target_pos.wy -= 0.03
        path_list = [list(target_pos.toVector())]
        motion_proxy.positionInterpolation(effector, frame, path_list, axis_mask, times, True)

        # swing LLeg forward
        times = [0.2, 0.3]  # seconds
        current_pos = motion_proxy.getPosition(effector, frame, use_sensor_values)
        target_pos = almath.Position6D(current_pos)
        target_pos.x += 0.15
        target_pos.wy -= 0.03
        path_list = [list(target_pos.toVector())]

        target_pos = almath.Position6D(current_pos)
        target_pos.x += 0.24
        target_pos.wy -= 0.03
        path_list.append(list(target_pos.toVector()))
        motion_proxy.positionInterpolation(effector, frame, path_list, axis_mask, times, True)