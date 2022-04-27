# import argparse
import imutils
import cv2

# image = cv2.imread("jpark.jpg")
image = cv2.imread("images/kirby.jpg")
mario = cv2.imread("images/mario.jpg")
# cv2.imshow("Image", image)
# cv2.waitKey(0)

image = imutils.resize(image, width=500)
# mario = imutils.resize(mario, width=500)
# cv2.imshow("Imutils Resize", resized)
# cv2.waitKey(0)

# ------------------------------ convert the image to grayscale ------------------------------ #
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# gray = cv2.cvtColor(mario, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)

# ------------------------------ edge detection ------------------------------ #
# edged = cv2.Canny(gray, 30, 150)
# cv2.imshow("Edged", edged)
# cv2.waitKey(0)

# ------------------------------ create mask ------------------------------ #
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]
# cv2.putText(thresh, "Here lies the mask", (0, 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)

# ------------------------------ contouring ------------------------------ #
# cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cnts = imutils.grab_contours(cnts)
# output = image.copy()
# # loop over the contours
# for c in cnts:
#     cv2.drawContours(output, [c], -1, (240, 0, 159), 3)
#     cv2.imshow("Contours", output)
# cv2.waitKey(0)

mask = thresh.copy()
output = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Output", output)
cv2.waitKey(0)
