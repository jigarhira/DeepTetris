import cv2
import numpy as np


def roi(image, vertices):

    # blank mask:
    mask = np.zeros_like(image)

    # filling pixels inside the polygon defined by "vertices" with the fill color
    cv2.fillPoly(mask, vertices, 255)

    # returning the image only where mask pixels are nonzero
    masked = cv2.bitwise_and(image, mask)
    return masked


def ProcessImage(image):

    processed_image = image

    #processed_image = cv2.cvtColor(original_image, cv2.COLOR_RGB2GRAY)
    #processed_image =  cv2.Canny(original_image, threshold1 = 75, threshold2=300)

    vertices = np.array([[40, 40], [200, 40], [200, 200], [40, 200]], np.int32)
    processed_image = processed_image[140:496, 100:280]


    return processed_image