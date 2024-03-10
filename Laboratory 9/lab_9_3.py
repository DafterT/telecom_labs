# %%
from thinkdsp import SquareSignal, decorate
# %%
in_wave = SquareSignal(freq=50).make_wave(duration=0.1, framerate=44100)
in_wave.plot()
decorate(xlabel='Time (s)')
# %%
out_wave = in_wave.cumsum()
out_wave.plot()
decorate(xlabel='Time (s)')
# %%
spectrum = in_wave.make_spectrum().integrate()
spectrum.hs[0] = 0
out_wave2 = spectrum.make_wave()
out_wave2.plot()
decorate(xlabel='Time (s)')
# %%
out_wave.unbias()
out_wave.normalize()
out_wave2.normalize()
out_wave.plot()
out_wave2.plot()
# %%
out_wave.max_diff(out_wave2)
# %%
