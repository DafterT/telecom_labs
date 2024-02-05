# %%
from thinkdsp import Sinusoid
from thinkdsp import normalize, unbias
import numpy as np

class SawtoothSignal(Sinusoid):
    
    def evaluate(self, ts):
        cycles = self.freq * ts + self.offset / np.pi / 2
        frac, _ = np.modf(cycles)
        ys = normalize(unbias(frac), self.amp)
        return ys

sawtooth = SawtoothSignal(200).make_wave(duration=0.5, framerate=40000)
sawtooth.segment(start=0, duration=0.005 * 4).plot()
# %%
spectrum = sawtooth.make_spectrum()
spectrum.plot(high=10000)
spectrum.peaks()[:10]
# %%
from thinkdsp import SquareSignal

sawtooth.make_spectrum().plot(high=10000, color='gray')
square = SquareSignal(freq=200, amp=0.5).make_wave(duration=0.5, framerate=40000)
sqere_spectrum = square.make_spectrum()
sqere_spectrum.plot(high=10000)
sqere_spectrum.peaks()[:10]
# %%
from thinkdsp import TriangleSignal

sawtooth.make_spectrum().plot(high=10000, color='gray')
triangle = TriangleSignal(freq=200, amp=0.78).make_wave(duration=0.5, framerate=40000)
triangle_spectrum = triangle.make_spectrum()
triangle_spectrum.plot(high=10000)
triangle_spectrum.peaks()[:10]
# %%
