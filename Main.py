from ThreadedTaskSubmitter import ThreadedTaskSubmitter
from TaskSubmitter import TaskSubmitter
from SoccerTask import SoccerTask
from NaoImageProcessor import NaoImageProcessor
from TemplateMatchingObjectDetector import TemplateMatchingObjectDetector
from naoqi import ALProxy
import cv2
import time


def main():
    # Load query images
    ballQueryImage = cv2.imread("./query_images/ball_query.png", cv2.IMREAD_COLOR)

    # Create the robot with the specified components
    threadedTaskSubmitter = ThreadedTaskSubmitter(TaskSubmitter())
    threadedTaskSubmitter.startNewTask(
        SoccerTask(
            NaoImageProcessor(
                TemplateMatchingObjectDetector(),
                ALProxy("ALVideoDevice", "127.0.0.1", 9560),
                cameraFPS=5
            ),
            ALProxy("ALMotion", "127.0.0.1", 9560),
            ALProxy("ALRobotPosture", "127.0.0.1", 9560),
            ballQueryImage
        )
    )
    print("waiting")
    threadedTaskSubmitter.waitTask()
    print("done waiting")
    #print("Started new task")
    #threadedTaskSubmitter.stopTask()


if __name__ == "__main__":
    main()