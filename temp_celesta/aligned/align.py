import sys

import cv2
import numpy as np

img_filename = sys.argv[1]
img2_filename = sys.argv[2]
output_filename = sys.argv[3]

img1_raw = cv2.imread(img_filename)
img2_raw = cv2.imread(img2_filename)

img1 = cv2.cvtColor(img1_raw, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2_raw, cv2.COLOR_BGR2GRAY)
height, width = img2.shape 

combined_img = np.full((height, width, 3), 0, np.uint8)
combined_img[:,:,1] = img1
combined_img[:,:,2] = img2

cv2.imwrite(output_filename, combined_img)
