# %%
from thinkdsp import SawtoothSignal, decorate
# %%
in_wave = SawtoothSignal(freq=50).make_wave(duration=0.1, framerate=44100)
in_wave.plot()
decorate(xlabel='Time (s)')
# %%
out_wave = in_wave.cumsum()
out_wave.unbias()
out_wave.plot()
decorate(xlabel='Time (s)')
# %%
out_wave = out_wave.cumsum()
out_wave.plot()
decorate(xlabel='Time (s)')
# %%
spectrum = in_wave.make_spectrum().integrate().integrate()
spectrum.hs[0] = 0
out_wave2 = spectrum.make_wave()
out_wave2.plot()
decorate(xlabel='Time (s)')
# %%
out_wave.make_spectrum().plot(high=500)