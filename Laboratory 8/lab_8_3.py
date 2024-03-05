# %%
from thinkdsp import SquareSignal, decorate, zero_pad
import numpy as np
import matplotlib.pyplot as plt
import scipy
# %%
M = 15
std = 2.5

gaussian = scipy.signal.windows.gaussian(M=M, std=std)   
bartlett = np.bartlett(M)
blackman = np.blackman(M)
hamming = np.hamming(M)
hanning = np.hanning(M)

windows = [blackman, gaussian, hanning, hamming]
names = ['blackman', 'gaussian', 'hanning', 'hamming']

for window in windows:
    window /= sum(window)
# %%
for window, name in zip(windows, names):
    plt.plot(window, label=name)

decorate(xlabel='Index')
# %%
def plot_window_dfts(windows, names):
    for window, name in zip(windows, names):
        padded =  zero_pad(window, 44100)
        dft_window = np.fft.rfft(padded)
        plt.plot(abs(dft_window), label=name)
# %%
plot_window_dfts(windows, names)
decorate(xlabel='Frequency (Hz)')
# %%
plot_window_dfts(windows, names)
decorate(xlabel='Frequency (Hz)', yscale='log')
# %%
