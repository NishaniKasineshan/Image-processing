import cv2
import numpy as np

HEIGHT=360
WIDTH=640

# Class visualization
mask = np.zeros((HEIGHT, WIDTH, 3))
print(type(mask),mask.shape)

img=cv2.imread("/assets/pic.jpg")
img=cv2.resize(img,(WIDTH,HEIGHT))
img=img.astype(np.uint8)
print(type(img),img.shape)


# Loop through each line coordinates and draw the lines on the image
cv2.line(mask, (50, 50), (200, 50), (0, 255, 0), 2) 
cv2.line(mask, (100, 150), (250, 150), (255,0, 0), 2)  
cv2.line(mask, (150, 250), (300, 250), (0, 0, 255), 2)  

mask=mask.astype(np.uint8)

# result = cv2.bitwise_and(mask, mask,mask= img[:,:,2])
dst = cv2.addWeighted(img, 1 , mask, 1, 0)
  


cv2.imshow("frame",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
