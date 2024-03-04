# %%
import numpy as np
import matplotlib.pyplot as plt

from thinkdsp import decorate
import scipy.signal.windows

from ipywidgets import interact
import ipywidgets as widgets
# %%
def plot_gaussian(std):
    M = 2 ** 5
    gaussian = scipy.signal.windows.gaussian(M=M, std=std)
    gaussian /= sum(gaussian)
    
    plt.subplot(1, 2, 1)
    plt.plot(gaussian)
    decorate(xlabel='Time')

    fft_gaussian = np.fft.fft(gaussian)
    fft_rolled = np.roll(fft_gaussian, M//2)
    
    plt.subplot(1, 2, 2)
    plt.plot(np.abs(fft_rolled))
    decorate(xlabel='Frequency')
    plt.show()

plot_gaussian(2)
# %%
slider = widgets.FloatSlider(min=0.1, max=20, value=2)
interact(plot_gaussian, std=slider)
# %%
