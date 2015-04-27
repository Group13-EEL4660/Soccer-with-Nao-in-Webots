import cv2


class TemplateMatchingObjectDetector():
    def __init__(self, queryThresholdDict):
        self.queryThresholdDict = queryThresholdDict
        pass

    def getResults(self, image, objectString):
        return cv2.matchTemplate(
            image,
            self.queryThresholdDict[objectString][0],
            cv2.TM_CCORR_NORMED
        )

    def objectLocationInImage(self, image, objectString, centroid=False):
        result = self.getResults(image, objectString)
        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
        if maxVal > self.queryThresholdDict[objectString][1]:
            if centroid:
                # Get the centroid of the query image and add that as an offset to maxLoc
                maxLoc = (maxLoc[0] + (self.queryThresholdDict[objectString][0].shape[1] / 2),
                          maxLoc[1] + (self.queryThresholdDict[objectString][0].shape[0] / 2))
            return maxLoc[0] / float(image.shape[1]), maxLoc[1] / float(image.shape[0])
        return None

    def percentageAboveThreshold(self, image, objectString):
        result = self.getResults(image, objectString)
        threshold = self.queryThresholdDict[objectString][1]
        squareArea = image.shape[1] * image.shape[0]
        print "Square area = " + str(squareArea)
        # Iterate through the results and count the number
        # of pixels that are above the threshold
        count = 0
        for score in result.flat:
            if score > threshold:
                count += 1
        return (count / float(squareArea)) * 100
