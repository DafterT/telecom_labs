# %%
import numpy as np
import matplotlib.pyplot as plt
from thinkdsp import decorate, Wave, zero_pad
import pandas as pd
# %%
df = pd.read_csv('FB_2.csv', header=0, parse_dates=[0])
ys = df['Close']
if len(ys) % 2:
    ys = ys[:-1]
in_wave = Wave(ys, framerate=1)
# %%
"""
from thinkdsp import SawtoothSignal

in_wave = SawtoothSignal(freq=50).make_wave(duration=0.1, framerate=44100)
in_wave.unbias()
in_wave.plot()
decorate(xlabel='Time (s)')
"""
# %%
in_wave.plot()
decorate(xlabel='Time (days)', ylabel='Price ($)')
# %%
in_spectrum = in_wave.make_spectrum()
in_spectrum.plot()
decorate(xlabel='Frequency (Hz)', ylabel='Amplitude')
# %%
out_wave = in_wave.cumsum()
out_wave.unbias()
out_wave.plot()
decorate(xlabel='Time (days)')
# %%
out_spectrum = out_wave.make_spectrum()
out_spectrum.plot()
decorate(xlabel='Frequency (Hz)', ylabel='Amplitude')
# %%
ratio_spectrum = out_spectrum.ratio(in_spectrum, thresh=1)
ratio_spectrum.plot(marker='.', ms=4, ls='')

decorate(xlabel='Frequency (Hz)',
         ylabel='Amplitude ratio',
         yscale='log')
# %%
# compute the diff filter
diff_window = np.array([1.0, -1.0])
padded = zero_pad(diff_window, len(in_wave))
diff_wave = Wave(padded, framerate=in_wave.framerate)
diff_filter = diff_wave.make_spectrum()
# compute the cumsum filter by inverting the diff filter
cumsum_filter = diff_filter.copy()
cumsum_filter.hs[1:] = 1 / cumsum_filter.hs[1:]
cumsum_filter.hs[0] = np.inf
# %%
cumsum_filter.plot(label='cumsum filter')
ratio_spectrum.plot(label='ratio', marker='.', ms=4, ls='')
decorate(xlabel='Frequency (Hz)',
         ylabel='Amplitude ratio',
         yscale='log')
# %%
out_wave.plot(label='summed', alpha=0.7)
cumsum_filter.hs[0] = 0
out_wave2 = (in_spectrum * cumsum_filter).make_wave()
out_wave2.plot(label='filtered', alpha=0.7)
decorate(xlabel='Time (days)')
# %%
out_wave.max_diff(out_wave2)