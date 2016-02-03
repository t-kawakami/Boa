__author__ = 'kawakami_note'

import numpy as np
import cv2
from matplotlib import pyplot as plt


def hist_mono():
    x = np.random.randint(25, 100, 25)
    y = np.random.randint(175, 255, 25)
    z = np.hstack((x, y))
    z = np.float32(z)
    z = z.reshape((50, 1))

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    flags = cv2.KMEANS_RANDOM_CENTERS
    compactness, labels, centers = cv2.kmeans(z, 2, None, criteria, 10, flags)
    A = z[labels == 0]
    B = z[labels == 1]

    plt.hist(A, 256, [0, 256], color='r')
    plt.hist(B, 256, [0, 256], color='b')
    plt.hist(centers, 32, [0, 256], color='y')
    plt.show()

def hist_multi():
    x = np.random.randint(25, 50, (25, 2))
    y = np.random.randint(60, 85, (20, 2))
    z = np.vstack((x, y))
    print(z)

if __name__ == '__main__':
    hist_multi()
