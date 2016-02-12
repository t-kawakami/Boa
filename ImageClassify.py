# -*- coding: utf-8 -*-
__author__ = 'kawakami'

import numpy as np
import csv
import cv2
import chainer.links as L
import chainer.functions as F
from chainer import Chain, optimizers, Variable

class Model(Chain):

    def __init__(self, input_num, unit_num, output_num):
        super(Model, self).__init__(
            l1=L.Linear(input_num, unit_num),
            l2=L.Linear(unit_num, unit_num),
            l3=L.Linear(unit_num, output_num)
        )

    def __call__(self, x):
        h1 = F.relu(self.l1(x))
        h2 = F.relu(self.l2(h1))
        y = self.l3(h2)
        return y

class Classifier(Chain):
    def __init__(self, predictor):
        super(Classifier, self).__init__(predictor=predictor)

    def __call__(self, x, t):
        y = self.predictor(x)
        self.loss = F.mean_squared_error(y, t)
        return self.loss

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

# 全画像のタグを集計し、各タグを0, 1の配列に変換する
def create_tag_map(img_tags):
    img_tag_list = []
    for img_tag in img_tags:
        tags = img_tags[img_tag].split(' ')
        for tag in tags:
            img_tag_list.append(tag)
    img_tag_set = list(set(img_tag_list))

    tag_map = {}
    for index in range(0, len(img_tag_set)):
        bi_array = np.array(np.zeros(len(img_tag_set)))
        bi_array.put(index, 1.0)
        tag_map[img_tag_set[index]] = bi_array
    return tag_map

# 各画像とタグ(0, 1の配列)とのマッピングを作る。複数のタグが紐づいているので、配列は縦に結合する
def create_img_tag_map(img_tags, tag_map):
    img_tag_map = {}
    for img_tag in img_tags:
        tags = img_tags[img_tag].split(' ')
        bi_array = np.array(np.zeros(len(tag_map)))
        for tag in tags:
            bi_array = np.add(bi_array, tag_map[tag])
        img_tag_map[img_tag] = bi_array
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
    tag_map = create_tag_map(img_tags)
    img_tag_map = create_img_tag_map(img_tags, tag_map)

    # 各特徴点をクラスタ化し、各クラスタの中心点を得る
    centers = create_cluster(np.float32(key_points_all))
    hists = create_hist(key_points, centers)

    # データセットを取得する
    x_all = np.array(hists.values()).astype(np.float32)
    y_all = np.array(img_tag_map.values()).astype(np.float32)

    data_size = int(len(x_all[0]) / 2)
    x_train, x_test = np.split(x_all, [data_size])
    y_train, y_test = np.split(y_all, [data_size])

    model = Classifier(Model(input_num=15,unit_num=20,output_num=len(y_all[0])))
    optimizer = optimizers.SGD()
    optimizer.setup(model)

    batch_size = 10
    sum_loss_train = 0
    sum_loss_test = 0
    for epoch in range(20):
        print('epoch %d' % epoch)
        indexes = np.random.permutation(data_size)
        for index in range(0, data_size, batch_size):
            x = Variable(x_train[indexes[index : index + batch_size]])
            t = Variable(y_train[indexes[index : index + batch_size]])
            optimizer.update(model, x, t)
            loss = model(x, t)
            sum_loss_train += loss.data * batch_size
            print('train loss : ', sum_loss_train)

        for index in range(0, 10, batch_size):
            x = Variable(x_test[index : index + batch_size])
            t = Variable(y_test[index : index + batch_size])
            loss = model(x, t)
            sum_loss_test += loss.data * batch_size
            print('test loss : ', sum_loss_test)

if __name__ == '__main__':
    main()
