import numpy as np
import cv2
import get_points
import os

# Define the region of interest (ROI)
x, y, w, h = 100, 950, 1650, 1700 

# Load image, grayscale, Otsu's threshold
directory = 'a'
str_list = os.listdir(directory)
image = cv2.imread('a/KEY.JPG')
ans = [cv2.imread('a/'+file_path) for file_path in str_list]

# Add ROI to the image
roi = image[y:y+h, x:x+w]

# Draw a red rectangle around the ROI
cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
cv2.imwrite('b/roi_demo.jpg', image)

gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Filter out large non-connecting objects
cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    area = cv2.contourArea(c)
    if area < 100:
        cv2.drawContours(thresh, [c], 0, 0, -1)

# Morph open using elliptical shaped kernel
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=3)

# Find circles
cnts = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    area = cv2.contourArea(c)
    if area > 500:
        ((x, y), r) = cv2.minEnclosingCircle(c)
        for idx, img in enumerate(ans):
            if img is not None:
                cv2.circle(img, (int(x), int(y)), int(r), (36, 255, 12), 2)
        cv2.circle(roi, (int(x), int(y)), int(r), (36, 255, 12), 2)

# Save the processed image
for i in range(len(str_list)):
    cv2.imwrite('b/'+str_list[i], ans[i])

cv2.waitKey()
