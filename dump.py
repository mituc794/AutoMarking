import numpy as np
import cv2
import get_points
import os
import img_process



# Define the region of interest (ROI)
x, y, w, h = 100, 950, 1650, 1700 

def check_matching_dots(dot_list1, dot_list2, threshold=10):
    matching_dots = []
    for (x1, y1, r1) in dot_list1:
        for (x2, y2, r2) in dot_list2:
            distance = np.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            if distance < threshold:
                matching_dots.append(((x1, y1, r1), (x2, y2, r2)))
    return matching_dots

# Load image, grayscale, Otsu's threshold
directory = 'a'
str_list = os.listdir(directory)
key_dot_list,_ = get_points.get_points('a/KEY.JPG')

for file_path in str_list:
    image = cv2.imread('a/'+file_path)
    dot_list,_ = get_points.get_points('a/'+file_path)
    matching_dots = check_matching_dots(key_dot_list, dot_list)
    print('Diem cua '+file_path+' la: ', len(matching_dots))
    img_process.img_process(key_dot_list, 'a/'+file_path)


cv2.waitKey()
