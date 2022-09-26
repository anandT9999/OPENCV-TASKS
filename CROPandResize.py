import cv2
import numpy as np

img = cv2.imread("C:\\Users\\torati.anand\\Desktop\\OpenCV\\TB_F_Clear.png")
print(img.shape)

imgResize = cv2.resize(img,(150,100))

imgCropped = img[0:200,0:200]
cv2.imshow("image",img)
cv2.imshow("resized",imgResize)
cv2.imshow("Cropped",imgCropped)
cv2.waitKey(0)