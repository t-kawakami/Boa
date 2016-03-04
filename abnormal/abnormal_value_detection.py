# -*- coding: utf-8 -*-
__author__ = 'kawakami_note'

import numpy as np
import scipy as sc
from scipy import linalg
from scipy import spatial
import scipy.spatial.distance
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager
import pylab

ROW = 10
COLUMN = 6
test_data = pd.read_csv('data/test.csv')

row, column = [], []
ave = [0.0 for index in xrange(ROW)]
vcm = np.zeros((COLUMN, ROW, ROW))
diff = np.zeros((1, ROW))
mahal = np.zeros(COLUMN)
tmp = np.zeros(ROW)

trans_data = test_data.dropna(axis=1)
print(trans_data)
