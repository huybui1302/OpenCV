import numpy as np
import matplotlib.pyplot as plt
import cv2

# ------------------------------ TEMPLATE MATCHING ------------------------------ #
# img_bgr = cv2.imread("find_waldo.png")
# img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
# template = cv2.imread("face.png", 0)
#
# w, h = template.shape[::-1]
#
# res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
# threshold = 0.8
# loc = np.where(res >= threshold)
# for pt in zip(*loc[::-1]):
#     cv2.rectangle(img_bgr, pt, (pt[0]+w, pt[1]+h), (0, 0, 255), 2)
# cv2.imshow("detected", img_bgr)

# ------------------------------ FEATURE MATCHING ------------------------------ #
# img1 = cv2.imread('mario_party.png')
# img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
# img2 = cv2.imread('mario_face.jpg')
# img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
#
# orb = cv2.ORB_create()
#
# kp1, des1 = orb.detectAndCompute(img1, None)
# kp2, des2 = orb.detectAndCompute(img2, None)
#
# bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
#
# matches = bf.match(des1, des2)
# matches = sorted(matches, key=lambda x: x.distance)
#
# img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)
# plt.imshow(img3)
# plt.show()

# ------------------------------ CORNER DETECTION ------------------------------ #
# img = cv2.imread('brutalist_architecture.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = np.float32(gray)
#
# corners = cv2.goodFeaturesToTrack(gray, 100, 0.1, 10)
# corners = np.int0(corners)
#
# for corner in corners:
#     x, y = corner.ravel()
#     cv2.circle(img, (x, y), 5, 255, 2)
# cv2.imshow('corner detection', img)

# cv2.waitKey(0)
