from RemoteNaoRobot import RemoteNaoRobot
from states.soccer.SoccerPrepState import SoccerPrepState
from TaskSubmitter import TaskSubmitter

def main():
    mainRobot = RemoteNaoRobot("127.0.0.1", 9560)
    taskSubmitter = TaskSubmitter(mainRobot)
    taskSubmitter.startNewTask(SoccerPrepState())


if __name__ == "__main__":
    main()