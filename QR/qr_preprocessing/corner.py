import cv2
import numpy as np

img = cv2.imread('cropped.jpg', cv2.IMREAD_ANYCOLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
filter_img = cv2.inRange(img, (0, 0, 0), (255, 150, 255))
# corner = cv2.cornerHarris(gray, 2, 3, 0.05)
corner = cv2.cornerHarris(filter_img, 2, 3, 0.05)
img[corner > 0.01*corner.max()] = [0, 255, 0]

corner_norm = cv2.normalize(corner, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

cv2.imshow('Harris', img)
cv2.imshow('corner', corner_norm)
cv2.waitKey()