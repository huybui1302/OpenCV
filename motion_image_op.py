import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()


def empty(a):
    pass


# ------------------------------ MANUAL COLOR ISOLATION ------------------------------ #
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640, 240)
cv2.createTrackbar("Hue min", "Trackbars", 0, 179, empty)
cv2.createTrackbar("Hue max", "Trackbars", 179, 179, empty)
cv2.createTrackbar("Sat min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Sat max", "Trackbars", 255, 255, empty)
cv2.createTrackbar("Val min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Val max", "Trackbars", 255, 255, empty)

while True:
    ret, frame = cap.read()
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# ------------------------------ COLOR ISOLATION ------------------------------ #
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # manual color isolation
    h_min = cv2.getTrackbarPos("Hue min", "Trackbars")
    h_max = cv2.getTrackbarPos("Hue max", "Trackbars")
    s_min = cv2.getTrackbarPos("Sat min", "Trackbars")
    s_max = cv2.getTrackbarPos("Sat max", "Trackbars")
    v_min = cv2.getTrackbarPos("Val min", "Trackbars")
    v_max = cv2.getTrackbarPos("Val max", "Trackbars")
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    # isolate blue
    # lower = np.array([90, 103, 0])
    # upper = np.array([180, 210, 255])
    # mask = cv2.inRange(hsv, lower, upper)

    # # isolate skin color
    # lower = np.array([0, 69, 35])
    # upper = np.array([30, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)

    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("res", res)

# ------------------------------ BLURRING AND SMOOTHING ------------------------------ #
#     gauss = cv2.GaussianBlur(res, (15, 15), 0)
#     median = cv2.medianBlur(res, 15)

    # kernel = np.ones((5, 5), np.uint8)
    # erosion = cv2.erode(mask, kernel, iterations=1)
    # dilation = cv2.dilate(mask, kernel, iterations=1)

    # cv2.imshow("gaussian", gauss)
    # cv2.imshow("median", median)
    # cv2.imshow("erosion", erosion)
    # cv2.imshow("dilation", dilation)

# ------------------------------ EDGE DETECTION ------------------------------ #
#     edges = cv2.Canny(frame, 100, 200)
#     cv2.imshow("edges", edges)

# ------------------------------ FOREGROUND EXTRACTION (VIA MOTION) ------------------------------ #
#     fg_mask = fgbg.apply(frame)
#
#     cv2.imshow('fg', fg_mask)
#
#     cv2.imshow("frame", frame)
#     # cv2.imshow("gray", gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
