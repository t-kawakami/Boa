import cv2
import os
import re


def detect_face():
    print("processing:" + img_dir + img_file + " with " + cascade_file)
    img = cv2.imread(img_dir + img_file)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier(cascade_dir + cascade_file)
    facerect = cascade.detectMultiScale(img_gray, scaleFactor=1.02, minNeighbors=1, minSize=(50, 50))

    if len(facerect) > 0:
        print("Faces are found in " + img_dir + img_file)
        print(facerect)
        for rect in facerect:
            cv2.rectangle(img, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), (255, 255, 255), thickness=2)
        print(dedicated_dir + str.replace(cascade_file, ".xml", "_") + img_file)
        cv2.imwrite(dedicated_dir + str.replace(cascade_file, ".xml", "_") + img_file, img)
    else:
        print("Faces are NOT found in " + img_dir + img_file)

cascade_dir = "./data/haarcascades/"
img_dir = "./data/image/"
#img_dir = "./data/movie/train/train/NG/"
dedicated_dir = "./data/movie/dedicated/"

cascade_files = [cascade_children for cascade_children in os.listdir(cascade_dir) if re.compile(".*test.*\.xml").match(cascade_children)]
img_files = [img_children for img_children in os.listdir(img_dir) if re.compile(".*\.png").match(img_children)]

for cascade_file in cascade_files:
    for img_file in img_files:
        detect_face()

