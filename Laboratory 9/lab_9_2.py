from thinkdsp import TriangleSignal, decorate
# %%
in_wave = TriangleSignal(freq=50).make_wave(duration=0.1, framerate=44100)
in_wave.plot()
decorate(xlabel='Time (s)')
# %%
out_wave = in_wave.diff()
out_wave.plot()
decorate(xlabel='Time (s)')
# %%
out_wave2 = in_wave.make_spectrum().differentiate().make_wave()
out_wave2.plot()
decorate(xlabel='Time (s)')