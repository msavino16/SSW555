import unittest

import os
import scipy.io as sio
import mne
from mne.datasets import sample

class testData(unittest.TestCase):
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