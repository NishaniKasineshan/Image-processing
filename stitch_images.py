import cv2
import numpy as np

front_camera=cv2.imread('./assets/center.jpg')
left_camera=cv2.imread('./assets/left.jpg')
right_camera=cv2.imread('./assets/right.jpg')

print(front_camera.shape)
print(left_camera.shape)
print(right_camera.shape)

# showing the original pictures
cv2.imshow('front_camera',front_camera)
cv2.imshow('left_camera',left_camera)
cv2.imshow('right_camera',right_camera)

stitched_view=cv2.Stitcher_create(cv2.Stitcher_SCANS)
status,stitched_op=stitched_view.stitch([left_camera,front_camera,right_camera])
print(stitched_op.shape)
if status != cv2.STITCHER_OK:
  # checking if the stitching procedure is successful
  # .stitch() function returns a true value if stitching is 
  # done successfully
  print(status)
  print("stitching ain't successful")
else: 
  print('Your Panorama is ready!!!')
  # final output
  cv2.imshow("stitched_image",stitched_op)

cv2.waitKey(0)
