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

# class TestCases(unittest.TestCase):

#     def testMin(self):
#         self.assertEqual(data_min, expected_min), "Test failed, data_min did not meet expected values"
    
#     def testMax(self):
#         self.assertEqual(data_max, expected_max), "Test failed, data_max did not meet expected values"


class TestMaxMinNormalizePositive(unittest.TestCase):

    def test_positive_values(self):
        data = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
        expected_result = np.array([[0.0, 0.5, 1.0],[0.0, 0.5, 1.0],[0.0, 0.5, 1.0]])
        result = max_min_normalize(data)
        self.assertTrue(np.allclose(result, expected_result), "Normalization failed for positive values")

class TestMaxMinNormalizeNegative(unittest.TestCase):
    def test_positive_values(self):
        data = np.array([[-1, -2, -3],[-4, -5, -6],[-7, -8, -9]])
        expected_result = np.array([[1.0, 0.5, 0],[1.0, 0.5, 0],[1.0, .5, 0]])
        result = max_min_normalize(data)
        self.assertTrue(np.allclose(result, expected_result), "Normalization failed for negative values")



class testData(unittest.TestCase):
    def testNormalize(self):
        data = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
        self.assertNoLogs(max_min_normalize(data))


    def testDataImport(self):
        data_path = sample.data_path()
        raw_fname = data_path / 'MEG' / 'sample' / 'sample_audvis_filt-0-40_raw.fif'
        self.assertNoLogs(mne.io.read_raw_fif(raw_fname, preload=True))

    def testDataFilter(self):
        data_path = sample.data_path()
        raw_fname = data_path / 'MEG' / 'sample' / 'sample_audvis_filt-0-40_raw.fif'
        raw = mne.io.read_raw_fif(raw_fname, preload=True)
        l_freq, h_freq = 1, 30
        self.assertNoLogs(raw.filter(l_freq, h_freq, method='fir', fir_design='firwin'))

    def testDataResampling(self):
        data_path = sample.data_path()
        raw_fname = data_path / 'MEG' / 'sample' / 'sample_audvis_filt-0-40_raw.fif'
        raw = mne.io.read_raw_fif(raw_fname, preload=True)
        l_freq, h_freq = 1, 30
        raw.filter(l_freq, h_freq, method='fir', fir_design='firwin')
        sfreq_resample = 480
        self.assertNoLogs(raw.resample(sfreq_resample))

    def testPlotEvents(self):
        data_path = sample.data_path()
        raw_fname = data_path / 'MEG' / 'sample' / 'sample_audvis_filt-0-40_raw.fif'
        raw = mne.io.read_raw_fif(raw_fname, preload=True)
        l_freq, h_freq = 1, 30
        raw.filter(l_freq, h_freq, method='fir', fir_design='firwin')
        sfreq_resample = 480
        raw = raw.resample(sfreq_resample)
        self.assertNoLogs(mne.find_events(raw, stim_channel="STI 014"))
        
    def testEEG1(self):
        data_path = sample.data_path()
        raw_fname = data_path / 'MEG' / 'sample' / 'sample_audvis_filt-0-40_raw.fif'
        raw = mne.io.read_raw_fif(raw_fname, preload=True)
        l_freq, h_freq = 1, 30
        raw.filter(l_freq, h_freq, method='fir', fir_design='firwin')
        sfreq_resample = 480
        raw = raw.resample(sfreq_resample)
        events = mne.find_events(raw, stim_channel="STI 014")
        event_id = 'LA'

        # set path to save data
        path = './data/real_data/'
        if not os.path.exists(path):
            os.makedirs(path)
        # fig_name = path + 'evoked_eeg_'+str(event_id)+'.png'
        # mat_name = path + 'evoked_eeg_'+str(event_id)+'.mat'
        self.assertNoLogs(path + 'evoked_eeg_'+str(event_id)+'.png')

    def testEEG2(self):
        data_path = sample.data_path()
        raw_fname = data_path / 'MEG' / 'sample' / 'sample_audvis_filt-0-40_raw.fif'
        raw = mne.io.read_raw_fif(raw_fname, preload=True)
        l_freq, h_freq = 1, 30
        raw.filter(l_freq, h_freq, method='fir', fir_design='firwin')
        sfreq_resample = 480
        raw = raw.resample(sfreq_resample)
        events = mne.find_events(raw, stim_channel="STI 014")
        event_id = 'LA'

        # set path to save data
        path = './data/real_data/'
        if not os.path.exists(path):
            os.makedirs(path)
        # fig_name = path + 'evoked_eeg_'+str(event_id)+'.png'
        # mat_name = path + 'evoked_eeg_'+str(event_id)+'.mat'
        self.assertNoLogs(path + 'evoked_eeg_'+str(event_id)+'.mat')

    def testEEG3(self):
        data_path = sample.data_path()
        raw_fname = data_path / 'MEG' / 'sample' / 'sample_audvis_filt-0-40_raw.fif'
        raw = mne.io.read_raw_fif(raw_fname, preload=True)
        l_freq, h_freq = 1, 30
        raw.filter(l_freq, h_freq, method='fir', fir_design='firwin')
        sfreq_resample = 480
        raw = raw.resample(sfreq_resample)
        events = mne.find_events(raw, stim_channel="STI 014")
        event_id = 'LA'

        # set path to save data
        path = './data/real_data/'
        if not os.path.exists(path):
            os.makedirs(path)
        fig_name = path + 'evoked_eeg_'+str(event_id)+'.png'
        mat_name = path + 'evoked_eeg_'+str(event_id)+'.mat'
        tmin = -0.1  # start of each epoch (100ms before the event)
        tmax = 0.4  # end of each epoch (400ms after the event)
        raw.info['bads'] = ['MEG 2443', 'EEG 053']
        baseline = (None, 0)  # means from the first instant to t = 0
        self.assertNoLogs(dict(grad=4000e-13, mag=4e-12, eog=150e-6))

if __name__ == '__main__':
    unittest.main()