import cv2
import pyzbar.pyzbar as pyzbar
import os
from glob import glob 

qr = cv2.QRCodeDetector()

img_f_path = 'qr_img'
fnames = glob(img_f_path + '/*')

for img in fnames:
    print(img)
    qr_img = cv2.imread(img)
    data, box, straight_qrcode = qr.detectAndDecode(qr_img)
    print(data)
    print()