import numpy as np

def check_matching_dots(dot_list1, dot_list2, threshold=10):
    matching_dots = []
    for (x1, y1, r1) in dot_list1:
        for (x2, y2, r2) in dot_list2:
            distance = np.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            if distance < threshold:
                matching_dots.append(((x1, y1, r1), (x2, y2, r2)))
    return matching_dots

def is_match(dot_1,dot_2,threshold =10):
    distance = np.sqrt((dot_1[0] - dot_2[0])**2 + (dot_1[1] - dot_2[1])**2)
    return distance < threshold