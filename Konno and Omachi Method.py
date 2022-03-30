# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 21:24:47 2020

@author: Santosh
"""


import obspy
from obspy.signal.konnoohmachismoothing import konno_ohmachi_smoothing
import obspy.signal.util
import numpy as np
from numpy.fft import rfft, rfftfreq
import matplotlib.pyplot as plt

st=obspy.read('c:\\PTN1504250611.su')
tr = st[0]

spec, freqs = rfft(tr.data)*tr.stats.delta, rfftfreq(tr.stats.npts, tr.stats.delta)

plt.figure(figsize=(12, 6))
plt.semilogx(freqs, np.abs(spec), label="raw", color="grey")


ko=konno_ohmachi_smoothing(abs(spec), freqs, normalize=True)
plt.semilogx(freqs,ko, label="konno ohmachi",color='red')

plt.legend()
plt.show()