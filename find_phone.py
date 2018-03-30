import numpy as np
import cv2
import sys


def find_center(img, CONSTRAST_THRESH, MIN_AREA, CANNY=False):

    MAX_AREA = 2500 # Area of contour
    CONTRAST = 5e4 # Minimum contrast
    DARKEN_THRESH = 85 # Fallback value for when original threshold produces featureless image

    width, height, depth = img.shape
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, gray = cv2.threshold(gray, CONSTRAST_THRESH, 255, cv2.THRESH_BINARY)

    #Narrower band when image appears too white
    if (width * height * np.max(img) - gray.sum()) < CONTRAST:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, gray = cv2.threshold(gray, DARKEN_THRESH, 255, cv2.THRESH_BINARY)

    gray = cv2.medianBlur(gray, 5)

    if CANNY: gray = cv2.Canny(gray, 50, 200)

    (_, contours, _) = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    center = None

    for cnt in contours:
        if MIN_AREA < cv2.contourArea(cnt) < MAX_AREA and len(cnt) >= 4:
            rect = cv2.boundingRect(cnt)
            temp_x, temp_y = int(rect[0] + rect[2] / 2), int(rect[1] + rect[3] / 2)
            x_norm, y_norm = temp_x / float(height), temp_y / float(width)

            center = [x_norm, y_norm] #TODO Find proper way of distinguishing which contour is most correct

    return center


if __name__ == "__main__":

    file_path = sys.argv[1]
    img = cv2.imread(file_path) # Load image

    #Check Image loaded properly
    if img is None: raise IOError("Image at location '{}' not found!".format(file_path))

    #First find the center with a stringent set of characteristics
    center = find_center(img, CONSTRAST_THRESH=30, MIN_AREA=220, CANNY=True)

    #If no phone is found then reduce thresholds
    if not center: center = find_center(img, CONSTRAST_THRESH= 50, MIN_AREA=10, CANNY=False)
    if not center: center = [0, 0]

    x, y = center

    print("{} {}".format(round(x, 4), round(y, 4)))


