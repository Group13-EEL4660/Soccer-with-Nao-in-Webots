from PIL import Image
import numpy as np
import vision_definitions


class NaoImageProcessor:
    def __init__(self,
                 objectDetector,
                 videoDevice,
                 cameraResolution=vision_definitions.kQVGA,
                 cameraColorSpace=vision_definitions.kBGRColorSpace,
                 cameraFPS=5):
        self.objectDetector = objectDetector
        self.videoDevice = videoDevice
        self.cameraResolution = cameraResolution
        self.cameraColorSpace = cameraColorSpace
        self.cameraFPS = cameraFPS
        self.cameraIndexToIDDict = {}  # Dictionary to map camera indexes to cameraIDs

    # Subscribe to all cameras that are in cameraIndexes
    def subscribe(self, cameraIndex):
        cameraId = self.videoDevice.subscribeCamera("NaoImgProcessor",
                                                    cameraIndex,
                                                    self.cameraResolution,
                                                    self.cameraColorSpace,
                                                    self.cameraFPS)
        self.cameraIndexToIDDict[cameraIndex] = cameraId

    # Unsubscribe from all cameras that are in cameraIndexes
    def unsubscribe(self, cameraIndex):
        try:
            cameraID = self.cameraIndexToIDDict[cameraIndex]
        except KeyError:
            return False
        self.videoDevice.unsubscribe(cameraID)
        return True

    def isSubscribed(self, cameraIndex):
        return cameraIndex in self.cameraIndexToIDDict

    # Returns the location of the object's centroid in the query image
    # if it is present. If it is not in the image, then None is returned.
    def objectLocationInCamera(self, cameraIndex, queryImg, threshold):
        try:
            cameraID = self.cameraIndexToIDDict[cameraIndex]
        except KeyError:
            # camera index not in the dictionary
            print("KEY ERROR")
            return None
        image = self.toNPArray(self.videoDevice.getImageRemote(cameraID))

        return self.objectDetector.objectLocationInImage(image, queryImg, threshold, True)

    def toNPArray(self, naoImage, colorSpaceStr="RGB"):
        imgWidth = naoImage[0]   # width
        imgHeight = naoImage[1]  # height
        imgData = naoImage[6]    # data

        pilImg = Image.frombytes(colorSpaceStr, (imgWidth, imgHeight), imgData)
        return np.array(pilImg)