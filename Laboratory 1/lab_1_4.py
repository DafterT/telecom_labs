# %%
from thinkdsp import read_wave

wave3 = read_wave('680840__seth_makes_sounds__homemade.wav')
wave3.normalize()
wave3.plot()
wave3.make_audio()
# %%
def stretch(wave, factor):
    wave.ts *= factor
    wave.framerate /= factor

stretch(wave3, 0.5)
wave3.make_audio()