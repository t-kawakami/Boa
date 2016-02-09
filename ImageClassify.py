# -*- coding: utf-8 -*-
__author__ = 'kawakami'

import numpy as np
import csv
import cv2

def create_hist(all_key_points, centers):
    hists = {}
    for key in all_key_points:
        hist = [0] * len(centers)
        for key_point in all_key_points[key]:
            min_dimension = -1
            min_index = 0
            index = 0
            for center in centers:
                dimension = np.sqrt(np.add(np.power(np.subtract(key_point[0], center[0]), 2),np.power(np.subtract(key_point[1], center[1]), 2)))
                if min_dimension == -1 or min_dimension > dimension:
                    min_dimension = dimension
                    min_index = index
                index += 1
            hist[min_index] += 1
        hists[key] = hist
    return hists

def create_cluster(key_points_all):
    # 特徴点をKMean法でクラスタ化
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    ret, label, center = cv2.kmeans(key_points_all, 15, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    return center

def extract_key_points(img_path):
    img = cv2.imread(img_path)
    detector = cv2.FastFeatureDetector_create()
    img_detects = detector.detect(img)
    key_points = []
    for img_detect in img_detects:
        key_points.append(img_detect.pt)
    return np.array(key_points)

def create_img_tag_map(img_tags):
    img_tag_list = []
    for img_tag in img_tags:
        tags = img_tags[img_tag].split(' ')
        for tag in tags:
            img_tag_list.append(tag)
    img_tag_set = list(set(img_tag_list))

    img_tag_map = {}
    for index in range(0, len(img_tag_set)):
        bi_array = np.array(np.zeros(len(img_tag_set)))
        bi_array.put(index, 1.0)
        img_tag_map[img_tag_set[index]] = bi_array
    return img_tag_map

def main():
    # 画像のデータファイル読み込み
    mapping_file = open('data/mapping.csv', 'r')
    reader = csv.reader(mapping_file)
    # 特徴点とタグを取得
    key_points = {}
    img_tags = {}
    key_points_all = np.array(np.zeros((0, 2)))
    for line in reader:
        key_points[line[0]] = extract_key_points(line[0])
        img_tags[line[0]] = line[1]
        key_points_all = np.vstack((key_points_all, key_points[line[0]]))
    # 各タグを0, 1に変換する
    img_tag_map = create_img_tag_map(img_tags)
    for img_tag in img_tag_map:
        print(img_tag, ':', img_tag_map[img_tag])

    # 各特徴点をクラスタ化し、各クラスタの中心点を得る
    centers = create_cluster(np.float32(key_points_all))
    hists = create_hist(key_points, centers)
    print(hists)

if __name__ == '__main__':
    main()
