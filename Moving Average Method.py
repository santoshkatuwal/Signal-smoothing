import obspy
#from obspy.signal.konnoohmachismoothing import konno_ohmachi_smoothing
import obspy.signal.util
import numpy as np
from numpy.fft import rfft, rfftfreq
import matplotlib.pyplot as plt

st=obspy.read('c:\\PTN1504250611.su')
tr = st[0]

spec, freqs = rfft(tr.data)*tr.stats.delta, rfftfreq(tr.stats.npts, tr.stats.delta)

plt.figure(figsize=(12, 6))
plt.semilogx(freqs, np.abs(spec), label="raw", color="grey")

m_av=obspy.signal.util.smooth(abs(spec), 5)
plt.semilogx(freqs,m_av, label="moving average",color='red')

plt.legend()
plt.show()