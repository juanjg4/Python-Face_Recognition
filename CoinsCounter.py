import cv2
import numpy as np

original_image = cv2.imread("coins.jpg")
gray_scale = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# Apply Gauss blur 
varGauss = 3
varKernel = 3
gauss_method = cv2.GaussianBlur(gray_scale, (varGauss, varKernel), 0)

# Apply Canny blur
canny_method = cv2.Canny(gauss_method, 60, 100)

# Show

cv2.imshow('Original Image', original_image)
cv2.imshow('Image in Gray scale', gray_scale)
cv2.imshow('Image after Gauss method', gauss_method)
cv2.imshow('Image after Canny method', canny_method)

cv2.waitKey(0)
cv2.destroyAllWindows()
