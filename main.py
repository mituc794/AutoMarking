import numpy as np
import cv2
import get_points
import os
import img_process
import map_matching
import getID


# Define the region of answer area
x_a, y_a, w_a, h_a = 100, 950, 1650, 1700 

#Define the region of ID area
x_i, y_i, w_i, h_i = 750, 250, 400, 600


# Load image, grayscale, Otsu's threshold
directory = 'a'
str_list = os.listdir(directory)
key_dot_list,_ = get_points.get_points('a/KEY.JPG')

for file_name in str_list:
    image = cv2.imread('a/'+file_name)
    dot_list,_ = get_points.get_points(file_path='a/'+file_name,have_roi=True)
    matching_dots = map_matching.check_matching_dots(key_dot_list, dot_list)
    id = getID.getID('a/'+file_name)
    print('Diem cua '+id+' la: ', len(matching_dots))
    img_process.img_process(key_dot_list, 'a/'+file_name,id )


cv2.waitKey()
