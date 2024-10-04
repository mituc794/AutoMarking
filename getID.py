import numpy as np
import cv2
import img_process
import map_matching
import get_points

def ID_map_test(test_image=False):
    # Two lines below are used to manually map the ID points
    #ls = get_points.get_points('E:\Workspace\Github\AutoMarking\ID_Map_2.jpg',0)
    #print(ls)


    #Modify this key_map to match the ID points
    key_map_1 = [(36, 553, 19), (34, 501, 18), (34, 458, 18), (33, 413, 18), (33, 366, 18), (35, 323, 18), (33, 278, 18), (34, 227, 18), (35, 184, 18), (34, 139, 18)]
    key_map_2 = [(80, 552, 18), (81, 506, 18), (79, 459, 18), (78, 411, 18), (78, 365, 18), (78, 321, 18), (78, 274, 18), (79, 227, 18), (79, 179, 18), (79, 132, 18)]
    key_map_3 = [(125, 552, 18), (124, 507, 18), (124, 460, 18), (124, 413, 18), (123, 366, 18), (123, 320, 18), (123, 275, 18), (123, 227, 18), (123, 181, 18), (123, 134, 18)]
    key_map_4 = [(172, 552, 18), (171, 507, 18), (171, 460, 18), (171, 413, 18), (171, 366, 18), (171, 320, 18), (171, 275, 18), (171, 227, 18), (171, 181, 18), (171, 134, 18)]
    key_map_5 = [(218, 552, 18), (218, 507, 18), (218, 460, 18), (218, 413, 18), (218, 366, 18), (218, 320, 18), (218, 275, 18), (218, 227, 18), (218, 181, 18), (218, 134, 18)]
    key_map_6 = [(264, 552, 18), (264, 507, 18), (264, 460, 18), (264, 413, 18), (264, 366, 18), (264, 320, 18), (264, 275, 18), (264, 227, 18), (264, 181, 18), (264, 134, 18)]
    key_map_7=[(310, 552, 18), (310, 507, 18), (310, 460, 18), (310, 413, 18), (310, 366, 18), (310, 320, 18), (310, 275, 18), (310, 227, 18), (310, 181, 18), (310, 134, 18)]
    key_map_8=[(356, 552, 18), (356, 507, 18), (356, 460, 18), (356, 413, 18), (356, 366, 18), (356, 320, 18), (356, 275, 18), (356, 227, 18), (356, 181, 18), (356, 134, 18)]
    
    key_map = []
    key_map.append(key_map_1)
    key_map.append(key_map_2)
    key_map.append(key_map_3)
    key_map.append(key_map_4)
    key_map.append(key_map_5)
    key_map.append(key_map_6)
    key_map.append(key_map_7)
    key_map.append(key_map_8)

    # Sort the key map by y coordinate
    for km in key_map:
        km.sort(key=lambda x: x[1])


    # Test the key map, draw the circles on the image
    if test_image:
        for key_map_i in key_map:
            img_process.img_process(key_map_i, 'map/res_mapping/roi.png', 'map/res_mapping')

    return key_map
    

def getID(file_path, x=750, y=250, w=400, h=600):
    # Load image, grayscale, Otsu's threshold
    image = cv2.imread(file_path)

    # Define the region of interest (ROI)
    roi = image[y:y+h, x:x+w]
    cv2.imwrite('map/res_mapping/ID_roi.jpg', roi)

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
            cv2.circle(image, (int(x)+750, int(y)+250), int(r), (255, 0, 0), 2)

    keymap = ID_map_test()
    dot_list.sort(key=lambda x: x[0])

    ID = ''
    for dot in dot_list:
        matched = False
        for i in range(8):
            for j in range(10):
                if map_matching.is_match(dot, keymap[i][j]):
                    ID += str(j)
                    matched = True
                    #break
            if matched:
                break
        if not matched:
            ID += 'x' 

    #cv2.imshow('image', image)
    #cv2.imwrite('ID.jpg', image)
    #cv2.waitKey()
    return ID

def getID_test(x, y, w, h):
    image = cv2.imread('map/src/ID_roi.jpg')
    roi = image[y:y+h, x:x+w]
    cv2.imwrite('map/res_mapping/ID_roi.jpg', roi)
    ls,_ = get_points.get_points('map/res_mapping/ID_roi.jpg', 0)
    img_process.img_process_4test(ls, 'map/res_mapping/ID_roi.jpg', 'map/res_mapping/')
    print(ls)
    return

#uncomment the line below to test the getID function
getID_test(750, 250, 400, 600)

