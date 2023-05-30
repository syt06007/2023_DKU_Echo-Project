import sys
import numpy as np
import cv2


src = cv2.imread('cropped.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

edges=cv2.Canny(src,50,155)
lines=cv2.HoughLinesP(edges,1.0,np.pi/180,160,minLineLength=50,maxLineGap=5)     
# lines = cv2.HoughLines(edges, 1, np.pi/180, 130)
#rho 값이 작으면 축적배열이 커지고 rho 값이 크면 축적배열이 작아진다. 
# 축적배열이 작아지면 시간은 빠르지만 정밀하지가 않다
#360도로 나누면 정교해지만 느리다
#threshold는 축적배열에서 몇 이상부터 직선으로 판단할지 임계값이다. threshold가 낮으면 많은 직선이 검출될수 있다.
#lines은 선분의 시작과 끝 좌표(x1,y1,x2,y2) shape=(N,1,4) 중간값은 무시
dst=cv2.cvtColor(edges,cv2.COLOR_GRAY2BGR)

if lines is not None:
    for i in range(lines.shape[0]):    #range(N)
        pt1=(lines[i][0][0],lines[i][0][1])
        pt2=(lines[i][0][2],lines[i][0][3])
        cv2.line(dst,pt1,pt2,(0,0,255),2,cv2.LINE_AA)


cv2.imshow('edges',edges)
print(lines)
cv2.imshow('dst',dst)
cv2.waitKey()