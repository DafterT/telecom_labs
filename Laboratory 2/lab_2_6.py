# %%
from thinkdsp import SinSignal
import numpy as np

freqs = np.arange(500, 9500, 500)
amps = (1 / freqs**2) * 10 ** 5
signal = sum(SinSignal(freq, amp) for freq, amp in zip(freqs, amps))
wave = signal.make_wave(duration=0.5, framerate=20000)
wave.segment(duration=0.01).plot()
wave.make_audio()
# %%
spectrum = wave.make_spectrum()
spectrum.plot()
spectrum.peaks()[:10]
# %%
