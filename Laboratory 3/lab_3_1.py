# %%
from thinkdsp import SinSignal
import matplotlib.pyplot as plt
import numpy as np

signal = SinSignal(freq=440)
duration = signal.period * 30.25
wave = signal.make_wave(duration)
spectrum = wave.make_spectrum()
spectrum.plot(high=880)
# %%
for window_func in [np.bartlett, np.blackman, np.hamming, np.hanning]:
    wave = signal.make_wave(duration)
    wave.ys *= window_func(len(wave.ys))

    spectrum = wave.make_spectrum()
    spectrum.plot(high=880, label=window_func.__name__)
plt.legend(loc='best')
plt.xlabel('Frequency (Hz)')
# %%
