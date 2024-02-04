# %%
from thinkdsp import read_wave

wave = read_wave('680840__seth_makes_sounds__homemade.wav')
wave.normalize()
wave.make_audio()
wave.plot()
# %%
segment = wave.segment(start=40.0, duration=0.5)
segment.make_audio()
segment.plot()
# %%
spectrum = segment.make_spectrum()
spectrum.plot(high=5000)
spectrum.make_wave().make_audio()
# %%
spectrum.low_pass(2000)
spectrum.plot(high=5000)
spectrum.make_wave().make_audio()
# %%
spectrum.high_pass(1000)
spectrum.plot(high=5000)
spectrum.make_wave().make_audio()
# %%
spectrum.band_stop(low_cutoff=100, high_cutoff=1000)
spectrum.plot(high=5000)
spectrum.make_wave().make_audio()
