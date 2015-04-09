from RemoteNaoRobot import RemoteNaoRobot
from states.soccer import SoccerPrepState


def main():
    mainRobot = RemoteNaoRobot("127.0.0.1", 9560)
    mainRobot.startNewTask(SoccerPrepState())


if __name__ == "__main__":
    main()