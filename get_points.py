import numpy as np
import cv2

def get_points(file_path, have_roi = True):
    if have_roi:
        # Load image, grayscale, Otsu's threshold
        image = cv2.imread(file_path)

        # Define the region of interest (ROI)
        x=100; y=950; w=1650; h=1700
        roi = image[y:y+h, x:x+w]

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
        dot_list = []
        for c in cnts:
            area = cv2.contourArea(c)
            if area > 500:
                ((x, y), r) = cv2.minEnclosingCircle(c)
                dot_list.append((int(x), int(y), int(r)))

        return dot_list,file_path
    else:
         # Load image, grayscale, Otsu's threshold
        image = cv2.imread(file_path)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
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
        dot_list = []
        for c in cnts:
            area = cv2.contourArea(c)
            if area > 500:
                ((x, y), r) = cv2.minEnclosingCircle(c)
                dot_list.append((int(x), int(y), int(r)))

        return dot_list,file_path

