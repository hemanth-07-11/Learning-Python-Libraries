import cv2 
import numpy as np                       
#print image

img = cv2.imread('D:\Hemanth\MIT ACADEMICS\VS CODE\pythprog\opencv\index.png',1)
cv2.imshow("img",img)                                                     ## opencv stores BGR image by default


#printing color image of an image
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow("bgr image",img2)                                    ## original image               ## Convert BGR to RGB image

#printing hsv image of an image
hsv_image = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)                   ## Convert BGR to HSV image 
cv2.imshow("hsv image",hsv_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
