import cv2

image = cv2.imread('shape.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresholdType,threshold = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

print(f'Threshold type: {thresholdType}')
# Show image
cv2.imshow('Original image', image)
cv2.imshow('Processed image: Gray', gray)
cv2.imshow('Processed image: Threshold', threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()

