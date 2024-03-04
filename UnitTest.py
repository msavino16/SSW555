import unittest
import warnings
warnings.simplefilter(action='ignore')
import scipy.io as sio
import scipy.io
import os
import sklearn
from sklearn import preprocessing
import numpy as np
import h5py
import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
from torch.autograd import Variable
import torch.nn.init
from torch.utils.data import Dataset, DataLoader
import mne
from mne.datasets import sample
import argparse
from argparse import ArgumentParser
from matplotlib import pylab as plt

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

def max_min_normalize(data):
    data_min = np.min(data, axis=1)
    data_max = np.max(data, axis=1)
    data_min = np.expand_dims(data_min, axis=1)
    data_max = np.expand_dims(data_max, axis=1)

    data_min = np.tile(data_min, (1, data.shape[1]))
    data_max = np.tile(data_max, (1, data.shape[1]))

    # data_normalized = (data - data_min) / (data_max - data_min)
    data_normalized = np.divide(data - data_min, data_max - data_min)
    return data_normalized

def min_normalize(data):
    data_min = np.min(data, axis=1)
    data_max = np.max(data, axis=1)
    data_min = np.expand_dims(data_min, axis=1)
    data_max = np.expand_dims(data_max, axis=1)

    data_min = np.tile(data_min, (1, data.shape[1]))
    data_max = np.tile(data_max, (1, data.shape[1]))

    # data_normalized = (data - data_min) / (data_max - data_min)
    data_normalized = np.divide(data - data_min, data_max - data_min)
    return data_min

def max_normalize(data):
    data_min = np.min(data, axis=1)
    data_max = np.max(data, axis=1)
    data_min = np.expand_dims(data_min, axis=1)
    data_max = np.expand_dims(data_max, axis=1)

    data_min = np.tile(data_min, (1, data.shape[1]))
    data_max = np.tile(data_max, (1, data.shape[1]))

    # data_normalized = (data - data_min) / (data_max - data_min)
    data_normalized = np.divide(data - data_min, data_max - data_min)
    return data_max

data = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])

data_min = min_normalize(data)
data_max = max_normalize(data)
expected_min = np.array([[1,1,1],[4,4,4],[7,7,7]])
expected_max = np.array([[3,3,3],[6,6,6],[9,9,9]])

class TestCases(unittest.TestCase):

    def testMin(self):
        self.assertEqual(data_min, expected_min), "Test failed, data_min did not meet expected values"
    
    def testMax(self):
        self.assertEqual(data_max, expected_max), "Test failed, data_max did not meet expected values"