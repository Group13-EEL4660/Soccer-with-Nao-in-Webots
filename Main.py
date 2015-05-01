from ThreadedTaskSubmitter import ThreadedTaskSubmitter
from TaskSubmitter import TaskSubmitter
from SoccerTask import SoccerTask
from NaoImageProcessor import NaoImageProcessor
from TemplateMatchingObjectDetector import TemplateMatchingObjectDetector
from naoqi import ALProxy
import cv2
from SoccerPositions import SoccerPositions


def main():
    # Load query images
    ballQueryImage = cv2.imread("./query_images/ball_query.png", cv2.IMREAD_COLOR)
    goalQueryImage = cv2.imread("./query_images/goal_query.png", cv2.IMREAD_COLOR)
    obstacleQueryImage = cv2.imread("./query_images/obstacle_query.png", cv2.IMREAD_COLOR)
    # Create the robot with the specified components
    threadedTaskSubmitterOffense = ThreadedTaskSubmitter(TaskSubmitter())
    threadedTaskSubmitterOffense.startNewTask(
        SoccerTask(
            NaoImageProcessor(
                TemplateMatchingObjectDetector({"Ball": (ballQueryImage, 0.9999),
                                                "Goal": (goalQueryImage, 0.9999),
                                                "Obstacle": (obstacleQueryImage, 0.91)}),
                ALProxy("ALVideoDevice", "127.0.0.1", 9560),
                cameraFPS=20
            ),
            ALProxy("ALMotion", "127.0.0.1", 9560),
            ALProxy("ALRobotPosture", "127.0.0.1", 9560),
            SoccerPositions.OFFENSE
        )
    )

    threadedTaskSubmitterDefense = ThreadedTaskSubmitter(TaskSubmitter())
    threadedTaskSubmitterDefense.startNewTask(
        SoccerTask(
            NaoImageProcessor(
                TemplateMatchingObjectDetector({"Ball": (ballQueryImage, 0.9999),
                                                "Goal": (goalQueryImage, 0.9999),
                                                "Obstacle": (obstacleQueryImage, 0.91)}),
                ALProxy("ALVideoDevice", "127.0.0.1", 9559),
                cameraFPS=5
            ),
            ALProxy("ALMotion", "127.0.0.1", 9559),
            ALProxy("ALRobotPosture", "127.0.0.1", 9559),
            SoccerPositions.DEFENSE
        )
    )

    threadedTaskSubmitterOffense.waitTask()
    threadedTaskSubmitterDefense.waitTask()


if __name__ == "__main__":
    main()