# %%
from thinkdsp import read_wave

wave = read_wave('680840__seth_makes_sounds__homemade.wav')
wave.normalize()
wave.plot()
wave.make_audio()
# %%
def stretch(wave, factor):
    wave.ts *= factor
    wave.framerate /= factor

stretch(wave, 0.5)
wave.plot()
wave.make_audio()