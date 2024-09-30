import get_points
import numpy as np

def check_matching_dots(dot_list1, dot_list2, threshold=10):
    matching_dots = []
    for (x1, y1, r1) in dot_list1:
        for (x2, y2, r2) in dot_list2:
            distance = np.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            if distance < threshold:
                matching_dots.append(((x1, y1, r1), (x2, y2, r2)))
    return matching_dots

img_a_dic = 'a/KEY.JPG'
img_b_dic = 'a/1.JPG'
dot_list_a, _ = get_points.get_points(img_a_dic)
dot_list_b, _ = get_points.get_points(img_b_dic)
matching_dots = check_matching_dots(dot_list_a, dot_list_b)
print('Do dai key la: ', len(dot_list_a))
print('Do dai 1 la: ', len(matching_dots))