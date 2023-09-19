import cv2

image = cv2.imread('shape.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresholdType,threshold = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

print(f'Threshold type: {thresholdType}')

contour, hierarchy = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contour, -1, (255,63,52), 3)
# Show image
cv2.imshow('Original image', image)
#cv2.imshow('Processed image: Gray', gray)
#cv2.imshow('Processed image: Threshold', threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()

