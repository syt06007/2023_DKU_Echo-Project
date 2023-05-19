import cv2

# read img
bgr_img = cv2.imread('cropped.jpg')

# img(BGR) to gray
gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)

# gray to Binary
ret, dst = cv2.threshold(gray_img, 100, 255, cv2.THRESH_BINARY)

# img save
cv2.imwrite("C:/Users/syt06/Desktop/KHS/window/qr_img/test.png", dst)

# img show
cv2.imshow('zz', dst)
cv2.waitKey(0)