from RemoteNaoRobot import RemoteNaoRobot
from states.soccer.SoccerPrepState import SoccerPrepState
from TaskSubmitter import TaskSubmitter
import time
from naoqi import ALProxy

def main():
    # Create the robot with the specified components
    mainRobot = RemoteNaoRobot.NaoRobotBuilder\
        .setMotion(ALProxy("ALMotion", "127.0.0.1", 9560))\
        .setRobotPosture(ALProxy("ALRobotPosture", "127.0.0.1", 9560))\
        .setVideoDevice(ALProxy("ALVideoDevice", "127.0.0.1", 9560))\
        .build()

    taskSubmitter = TaskSubmitter(mainRobot)
    taskSubmitter.startNewTask(SoccerPrepState())
    print("Passed start task")
    time.sleep(5)
    taskSubmitter.startNewTask(SoccerPrepState())
    print("Started new task")
    taskSubmitter.stopTask()


if __name__ == "__main__":
    main()