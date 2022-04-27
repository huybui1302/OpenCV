import imutils
import cv2

image = cv2.imread("images/jpark.jpg")
(h, w, d) = image.shape
# print("width={}, height={}, depth={}".format(w, h, d))
# (B, G, R) = image[100, 50]
# print("R={}, G={}, B={}".format(R, G, B))

# cv2.imshow("Image", image)
# cv2.waitKey(0)

# # ------------------------------ CROP ------------------------------ #
# roi = image[100:700, 480:900]
# cv2.imshow("ROI", roi)
# cv2.waitKey(0)

# # ------------------------------ RESIZE ------------------------------ #
# resized = cv2.resize(image, (1000, 500))
# cv2.imshow("Fixed Resizing", resized)
# cv2.waitKey(0)

# # ------------------------------ RESIZE WITH ASPECT RATIO ------------------------------ #
# resized = imutils.resize(image, width=300)
# cv2.imshow("Imutils Resize", resized)
# cv2.waitKey(0)

# # ------------------------------ ROTATE ------------------------------ #
# center = (w // 2, h // 2)
# M = cv2.getRotationMatrix2D(center, -45, 1.0)
# rotated = cv2.warpAffine(image, M, (w, h))
# cv2.imshow("OpenCV Rotation", rotated)
# cv2.waitKey(0)

# # ------------------------------ DRAW A RECTANGLE AROUND THE FACE `1 ------------------------------ #
output = image.copy()
cv2.rectangle(output, (480, 100), (900, 700), (0, 0, 255), 2)
cv2.imshow("Rectangle", output)
cv2.waitKey(0)
