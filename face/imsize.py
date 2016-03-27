import cv2
import os
import re

img_dir = './data/movie/train_hack/OK/'

img_files = [img_children for img_children in os.listdir(img_dir) if re.compile(".*\.png").match(img_children)]

for img_file in img_files:
    img = cv2.imread(img_dir + img_file)
    height, width, channels = img.shape
    print (img_dir + img_file).replace('/', '\\'), 1, 20, 20, height, width