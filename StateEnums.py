from enum import Enum


class StateEnums(Enum):
    PREPARE_TO_PLAY = 0
    WANDER_FOR_BALL = 1
    FOLLOW_BALL = 2
    ALIGN_BALL_WITH_GOAL = 3
    KICK_BALL = 4