# %%
from thinkdsp import Noise
import numpy as np
import matplotlib.pyplot as plt

class UncorrelatedPoissonNoise(Noise):

    def evaluate(self, ts):
        ys = np.random.poisson(self.amp, len(ts))
        return ys
# %%
amp = 0.001
framerate = 10000
duration = 30

signal = UncorrelatedPoissonNoise(amp=amp)
wave = signal.make_wave(duration=duration, framerate=framerate)
wave.make_audio()
# %%
wave.plot()
plt.show()
wave.segment(start=0, duration=1).plot()
plt.show()
# %%
from thinkdsp import decorate

spectrum = wave.make_spectrum()
spectrum.plot_power()
decorate(xlabel='Frequency (Hz)',
         ylabel='Power',
         xscale='log', 
         yscale='log')

# %%
spectrum.estimate_slope().slope
# %%
