# %%
from thinkdsp import SquareSignal

square = SquareSignal(1100).make_wave(duration=0.5, framerate=10000)
square_spectrum = square.make_spectrum()
square_spectrum.plot()
square_spectrum.peaks()[:10]
# %%
square.make_audio()
# %%
from thinkdsp import SinSignal

SinSignal(2300).make_wave(duration=0.5, framerate=10000).make_audio()
# %%
SinSignal(100).make_wave(duration=0.5, framerate=10000).make_audio()
# %%
