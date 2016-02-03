# -*- coding: utf-8 -*-
__author__ = 'kawakami'

import numpy as np
import csv
import cv2

def create_hist(key_points_all):
    # 特徴点をKMean法でクラスタ化
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    ret, label, center = cv2.kmeans(key_points_all, 15, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    a = key_points_all[label.ravel() == 0]
    b = key_points_all[label.ravel() == 1]


def extract_key_points(img_path):
    img = cv2.imread(img_path)
    detector = cv2.FastFeatureDetector_create()
    img_detects = detector.detect(img)
    return np.array(img_detect.pt for img_detect in img_detects)

if __name__ == '__main__':
    # 画像のデータファイル読み込み
    mapping_file = open('data/mapping.csv', 'r')
    reader = csv.reader(mapping_file)
    index = 0
    # 特徴点とタグを取得
    key_points = {}
    img_tags = {}
    for line in reader:
        key_points[line[0]] = extract_key_points(line[0])
        img_tags[line[0]] = line[1]
        key_points['all'] = np.vstack(np.append(key_points[line[0]]))

    create_hist(key_points['all'])
