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
    
    # Save the processed image in the 'b/' directory with the same filename
    processed_image_path = os.path.join(output_dir, os.path.basename(image_path))
    cv2.imwrite(processed_image_path, image)
    
