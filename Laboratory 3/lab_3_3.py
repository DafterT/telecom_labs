# %%
from lab_3_2 import SawtoothChirp

signal = SawtoothChirp(start=2500, end=3000)
wave = signal.make_wave(duration=1, framerate=20000)
wave.make_spectrum().plot(scalex=500)
wave.make_audio()
# %%
