import cv2


class TemplateMatchingObjectDetector():
    def __init__(self):
        pass

    def objectLocationInImage(self, image, queryImage, threshold, centroid=False):
        result = cv2.matchTemplate(image, queryImage, cv2.TM_CCORR_NORMED)
        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
        if maxVal > threshold:
            if centroid:
                # Get the centroid of the query image and add that as an offset to maxLoc
                maxLoc = (maxLoc[0] + (queryImage.shape[1] / 2),
                          maxLoc[1] + (queryImage.shape[0] / 2))
            return maxLoc[0] / float(image.shape[1]), maxLoc[1] / float(image.shape[0])
        return None