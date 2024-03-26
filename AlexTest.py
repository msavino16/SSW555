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
