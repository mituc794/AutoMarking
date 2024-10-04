import numpy as np
import cv2
import os
import get_points

def img_process(dot_list, image_path):
    
    # Load the image
    image = cv2.imread(image_path)
    
    # Draw circles on the image
    for (x, y, r) in dot_list:
        cv2.circle(image, (x, y), r, (36, 255, 12), 2)
    
    # Create the output directory if it doesn't exist
    output_dir = 'b/'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print('Directory not found. Created a new directory:', output_dir)
    
    # Save the processed image in the 'b/' directory with the same filename
    processed_image_path = os.path.join(output_dir, os.path.basename(image_path))
    cv2.imwrite(processed_image_path, image)

def img_process(dot_list, src_image_path, id):
    
    # Load the image
    image = cv2.imread(src_image_path)

    x_a, y_a, w_a, h_a = 100, 950, 1650, 1700 
    
    # Draw circles on the image
    for (x, y, r) in dot_list:
        cv2.circle(image, (x+x_a, y+y_a), r, (36, 255, 12), thickness=2) #thickness=2, thickness=-1 to fill
    
    
    # Save the processed image in the 'b/' directory with the same filename
    processed_image_path = 'b/'+id+'.jpg'
    cv2.imwrite(processed_image_path, image)
    print('Image processed and saved to:', processed_image_path)
    
def img_process_4test(dot_list, src_image_path, dst_image_path):
    
    # Load the image
    image = cv2.imread(src_image_path)

    
    # Draw circles on the image
    for (x, y, r) in dot_list:
        cv2.circle(image, (x, y), r, (36, 255, 12), thickness=2) #thickness=2, thickness=-1 to fill
    
    
    # Save the processed image in the 'b/' directory with the same filename
    processed_image_path = dst_image_path+'test.jpg'
    cv2.imwrite(processed_image_path, image)
    print('Image processed and saved to:', processed_image_path)