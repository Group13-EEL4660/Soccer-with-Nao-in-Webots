from enum import Enum


class StateEnums(Enum):
    PREPARE_TO_PLAY = 0
    WANDER_FOR_BALL = 1
    FOLLOW_BALL = 2
    APPROACH_BALL = 3
    ALIGN_BALL_WITH_GOAL = 4
    KICK_BALL = 5
    DRIBBLE_BALL = 6
    AVOID_OBSTACLE = 7
    DEFEND_GOAL = 8